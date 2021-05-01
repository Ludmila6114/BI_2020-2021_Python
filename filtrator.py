import sys
import os
from sys import stdout, stdin

def parser(argv = sys.argv):
    def is_a_number(input):
        try:
            float(input)
            return True
        except ValueError:
            return False

    keep_filtered = False
    min_length = 0
    gc_low = 0
    gc_high = 100
    output_base_name = ''
    if len(argv) == 2:
        file_name = argv[1]
    else:
        i = 1
        while i < len(argv) - 1:
            if argv[i] == '--min_length':
                min_length = argv[i+1]
                i += 2
            elif argv[i] == '--keep_filtered':
                keep_filtered = True
                i += 1
            elif argv[i] == '--gc_bounds':
                if is_a_number(argv[i+1]):
                    gc_low = float(argv[i+1])
                    if is_a_number(argv[i+2]):
                        gc_high = float(argv[i+2])
                        i += 3
                    else:
                        i += 2
                else:
                    i += 1
            elif sys.argv[i] == '--output_base_name':
                output_base_name = argv[i+1]
                i += 2
        file_name = sys.argv[len(argv) - 1]
    if output_base_name == '':
        file_name_list = [x for x in file_name]
        output_base_name = ''.join(file_name_list[0: len(file_name_list) - 6])
    return file_name, keep_filtered, min_length, gc_low, gc_high, output_base_name


file_name, keep_filtered, min_length, gc_low, gc_high, output_base_name = parser(sys.argv)
print(f"Launch status: File name: {file_name}, keep filtered: {keep_filtered}, min length = {min_length}, GC min = {gc_low}, GC max = {gc_high}, output base name: {output_base_name}")



def filtrator(file_name = file_name, keep_filtered = keep_filtered, min_length = min_length, gc_low = gc_low, gc_high = gc_high, output_base_name = output_base_name):
    if keep_filtered == True:
        filtered = output_base_name + '_failed.fastq'
        filtered_reads = open(filtered, 'a')
    passed = output_base_name + '_passed.fastq'
    passed_reads = open(passed, 'a')
    with open(file_name) as fastq:
        Length = -1
        while Length != 0:
            name = fastq.readline()
            sequence = fastq.readline().strip()
            comment = fastq.readline().strip()
            quality = fastq.readline().strip()
            GC_total = sequence.count('G') + sequence.count('C')
            Length = len(sequence)
            if Length != 0:
                GC_content = GC_total/Length * 100
                if Length >= int(min_length) and GC_content >= gc_low and GC_content <= gc_high:
                    passed_reads.writelines(name)
                    passed_reads.writelines(sequence+'\n')
                    passed_reads.writelines(comment+'\n')
                    passed_reads.writelines(quality+'\n')
                else:
                    if keep_filtered == True:
                        filtered_reads.writelines(name)
                        filtered_reads.writelines(sequence+'\n')
                        filtered_reads.writelines(comment+'\n')
                        filtered_reads.writelines(quality+'\n')

    passed_reads.close()
    if keep_filtered == True:
        filtered_reads.close()

    return passed

filtrator()

import unittest
class Tests(unittest.TestCase):
    #Тест на инициализацию переменных
    def test_init(self):
        #Если задаем параметры:
        file_name, keep_filtered, min_length, gc_low, gc_high, output_base_name = parser(['./filtrator.py', '--min_length', '10', '--keep_filtered', '--gc_bounds', '10', '50', '--output_base_name', 'haha', 'small_data.fastq'])
        self.assertEqual(file_name, 'small_data.fastq')
        self.assertEqual(keep_filtered, 'True')
        self.assertEqual(min_length, '10')
        self.assertEqual(gc_low, 10.0)
        self.assertEqual(gc_high, 50.0)
        self.assertEqual(output_base_name, 'haha')
        #Тест на дефолтные параметры:
        file_name, keep_filtered, min_length, gc_low, gc_high, output_base_name = parser(['./filtrator.py', 'small_data.fastq'])
        self.assertEqual(file_name, 'small_data.fastq')
        self.assertEqual(keep_filtered, False)
        self.assertEqual(min_length, 0)
        self.assertEqual(gc_low, 0)
        self.assertEqual(gc_high, 100)
        self.assertEqual(output_base_name, 'small_data')


    def test_filtrator(self, data = ['./filtrator.py', '--min_length', '10', '--keep_filtered', '--gc_bounds', '10', '50', '--output_base_name', 'haha', 'small_data.fastq']):
        file_name, keep_filtered, min_length, gc_low, gc_high, output_base_name = parser(data)
        print(file_name, keep_filtered, min_length, gc_low, gc_high, output_base_name)
        passed = filtrator(file_name, keep_filtered, min_length, gc_low, gc_high, output_base_name)
        f = open(passed, "r")
        self.assertEqual(f.readline(), '@SRR1363257.46 GWZHISEQ01:153:C1W31ACXX:5:1101:19721:2155 length=101\n')
        self.assertEqual(f.readline(), 'GTATGAGGTTTTGCTGCATTCTCTGNGCGAATATTAACTCCNTNNNNNTTATAGTTCAAAGCAAGTACCTGTCTCTTATACACATCTCCGAGCCCACGAGC\n')
        self.assertEqual(f.readline(), '+\n')
        self.assertEqual(f.readline(), '@@<?=D?D==?<AFGDF+AIHEACH#22<:?E8??:9??GG#0#####000;CF=C)4.==CA@@@)=7?C7?E37;3@>;;(.;>AB#############\n')
        f.close()
        os.remove(passed)

        return



