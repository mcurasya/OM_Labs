class matrix:
  def init(self, matr):
    self.matrix = matr[::]
  
  def __mul__(self, other):
    