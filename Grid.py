class Grid:
	def __init__(self, cell_size, screen_size):
		self.cell_size = cell_size
		self.rows = screen_size[0] // self.cell_size
		self.cols = screen_size[1] // self.cell_size
		self.cell_data = {}

	def update_cell_data(self, row, col, color):
		if(row in range(0, self.rows + 1) and col in range(0, self.cols + 1)):
			self.cell_data[(row, col)] = color
		else:
			raise ValueError(f"Given row/column (row {row}, col {col}) doesn't exist!")

	def clear_cell_data(self):
		self.cell_data.clear()

	def draw_cells(self, surface):
		for cell in self.cell_data:
			self._fill(surface, cell[0], cell[1], self.cell_data[cell])

	def _fill(self, surface, row, col, color):
		surface.fill(color, (0 + self.cell_size * col, 0 + self.cell_size * row, self.cell_size + 1, self.cell_size + 1))

	def __str__(self):
		return f"Grid(cell_size={self.cell_size}, rows={self.rows}, cols={self.cols})"
