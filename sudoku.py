
import random


class Grid:
    def __init__(self):
        """Generation of the base table"""
		self.table = [[((i*3 + i/3 + j) % (9) + 1) for j in range(9)] for i in range(9)]
        
    def transposing(self):
        """Transposing the whole grid """
		self.table = map(list, zip(*self.table))
        
    def swap_rows_small(self):
		""" Swap the two rows """
		area = random.randrange(0,3,1)
		line1 = random.randrange(0,3,1)
		#получение случайного района и случайной строки
		N1 = area*3 + line1
		#номер 1 строки для обмена
        
		line2 = random.randrange(0,3,1)
		while (line1 == line2):
			line2 = random.randrange(0,3,1)

		N2 = area*3 + line2
		#номер 2 строки для обмена

		self.table[N1],self.table[N2] = self.table[N2], self.table[N1]
        
    def swap_rows_area(self):
		""" Swap the two area horizon """
		area1 = random.randrange(0,3,1)
		#получение случайного района

		area2 = random.randrange(0,3,1)
		while (area1 == area2):
			area2 = random.randrange(0,3,1)

		for i in range(0, 3):
			N1, N2 = area1*3 + i, area2*3 + i
			self.table[N1], self.table[N2] = self.table[N2], self.table[N1]
            
    def swap_colums_small(self):
		grid.transposing(self)
		grid.swap_rows_area(self)
		grid.transposing(self)
        
    def swap_colums_small(self):
		grid.transposing(self)
		grid.swap_rows_area(self)
		grid.transposing(self)
        
    def mix(self,amt = 10):
		mix_func = ['self.transposing()', 
					'self.swap_rows_small()', 
					'self.swap_colums_small()', 
					'self.swap_rows_area()', 
					'self.swap_colums_area()']
		for i in xrange(1, amt):
			id_func = random.randrange(0,len(mix_func),1)
			eval(mix_func[id_func])
	
	def show(self):
		for i in range(9):
			print self.table[i]


class Sudoku(Grid):    
    def __init__(self):
        super().__init__(self)
        
    def del_cell(self):
		for t in range(self.d) 
            i, j = random.randrange(0, 9, 1), random.randrange(0, 9, 1)
            if self.grid[i][j] != '':
                self.grid[i][j] = ''
            else:
               t -= 1
        
    def _generate_field(self, del_count):
        self.mix()
        self.dell(del_count)
            
    def _check_step(self, line, column, val):
        i = line//3
        j = column//3
        if (val in self.grid[line][:]) or:
            (val in self.grid[:][line]) or
            (val in self.grid[i*3:(i+1)*3][j*3:(j+1)*3]):
                return False
        return True
        
        
    def _check_fill(self):
        if '' not in self.grid
        
    
    def get_start(self):
        cell_count = input('Введите колличество заполненых ячеек: ')
        self.generate_field(81 - cell_count)
        
    def get_step(self, line, column, val):
        if self.check_step(line, column, val):
            self.field[line][column] = val
        else:
            print('wrong value')
        if self.check_fill():
            print('')
            
            
def main():
    
            
            
if __name__ == '__main__':
    main()
        
            
    
        
    
        
