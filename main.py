import pygame
import colors
from sys import exit as EXIT
from Grid import Grid


class App:
	def __init__(self, title="pygame window", screen_size=(1080, 720), FPS=60):
		"""
		Initialization
		"""
		self.SCREENWIDTH = screen_size[0]
		self.SCREENHEIGHT = screen_size[1]
		self.title = title
		self.FPS = FPS
		self.grid = Grid(40, screen_size)
		print(self.grid)

		pygame.init()
		self.game_display = pygame.display.set_mode(screen_size)
		pygame.display.set_caption(self.title)
		self.CLOCK = pygame.time.Clock()

	def main(self):
		"""
		Main function
		"""
		col = 0
		row = 0
		cell_diff = 0
		direction = "right"
		color = colors.random_color(excludes=[colors.black])
		run = True
		while run:
			# ticking the FPS
			dt = self.CLOCK.tick(self.FPS)

			# event section start
			for event in pygame.event.get():
				if(event.type == pygame.QUIT):
					pygame.quit()
					EXIT()
			# event section end

			self.game_display.fill(colors.black)

			# updating the cell data (reseting if needed)
			if(cell_diff <= self.grid.cols // 2 - 1):
				self.grid.update_cell_data(row, col, color)
			else:
				pygame.time.delay(300)
				col = 0
				row = 0
				cell_diff = 0
				direction = "right"
				color = colors.random_color(excludes=[colors.black])
				self.grid.clear_cell_data()
				self.grid.update_cell_data(row, col, color)

			# try:
			# 	self.grid.update_cell_data(row, col, color)
			# except ValueError:
			# 	col = 0
			# 	row = 0
			# 	cell_diff = 0
			# 	direction = "right"
			# 	color = colors.random_color(excludes=[colors.black])
			# 	self.grid.clear_cell_data()
			# 	self.grid.update_cell_data(row, col, color)

			# drawing all the cells on the grid
			self.grid.draw_cells(self.game_display)

			if(direction == "right"):
				col += 1

				if(col >= self.grid.cols - 1 - cell_diff):
					direction = "down"
			elif(direction == "down"):
				row += 1

				if(row >= self.grid.rows - 1 - cell_diff):
					direction = "left"
			elif(direction == "left"):
				col -= 1

				if(col <= 0 + cell_diff):
					direction = "top"
			elif(direction == "top"):
				row -= 1

				if(row <= 0 + cell_diff):
					direction = "right"
					col += 1
					row += 1
					cell_diff += 1
					color = colors.random_color(excludes=[colors.black])
			else:
				raise ValueError("Invalid direction value!")

			# updating the game display surface
			pygame.display.update()
