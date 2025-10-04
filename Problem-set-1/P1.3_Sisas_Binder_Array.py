class Sisas_Binder_Array:
    def __init__(self, x):
        self.array_X
        self.array_Y # Circular array representing the pages between the bookmarks A and B
        self.first_index_in_Y
        self.A = -2 # Allowed range [-1, n]
        self.B = -2 # Allowed range [-1, n]

    def build(self, X):
        self.array_X = [x for x in X] # Equivalent to list(X)
        self.array_Y = [x for x in X]

    def place_mark(self, i, m):
        if not self._is_bookmarks_placed():
            if m == 'A':
                self.A = i
                self.first_index_in_Y = i + 1
            elif m == 'B':
                self.B = i
        else:
            if m == 'A':
                moves = m - self.A
                direction = 1 if moves > 0 else -1
                for _ in range(abs(moves)):
                    self.shift_mark('A', direction)
            elif m == 'B':
                moves = m - self.B
                direction = 1 if moves > 0 else -1
                for _ in range(abs(moves)):
                    self.shift_mark('B', direction)

    def read_page(self, i):
        if (i <= self.A or i > self.B):
            return self.array_X[i]
        else:
            page_in_Y_index = (self.first_index_in_Y + i - self.A - 1) % len(self.array_Y) # Considers the cyclic boundary
            return self.array_Y[page_in_Y_index]

    def shift_mark(self, m, d):
        if not self._is_bookmarks_placed():
            return

        if m == 'A':
            if (d == 1):
                if (self.A == self.B):
                    return
                self.A += 1
                self.array_X[self.A] = self.array_Y[self.first_index_in_Y]
                self.first_index_in_Y = (self.first_index_in_Y + d) % len(self.array_Y)

            elif (d == -1):
                if (self.A == -1):
                    return
                self.first_index_in_Y = (self.first_index_in_Y + d) % len(self.array_Y)
                self.array_Y[self.first_index_in_Y] = self.array_X[self.A]
                self.A -= 1

        elif m == 'B':
            if (d == 1):
                if (self.B == len(self.X)):
                    return
                n_pages_between_bookmarks = self.B - self.A
                insert_index = (self.first_index_in_Y + n_pages_between_bookmarks) % len(self.array_Y)
                self.array_Y[insert_index] = self.X[self.B+1]
                self.B += 1
            if (d == -1):
                if (self.A == self.B):
                    return
                n_pages_between_bookmarks = self.B - self.A
                page_front_of_B_index = (self.first_index_in_Y + n_pages_between_bookmarks - 1) % len(self.array_Y)
                self.X[self.B] = self.array_Y[page_front_of_B_index]
                self.B -= 1

    def move_page(self, m):
        if not self._is_bookmarks_placed():
            return

        n_pages_between_bookmarks = self.B - self.A
        if n_pages_between_bookmarks == 0:
            return

        if m == 'A': # Move from A to B
            if self.A == -1: # No page in front of A
                return
            insert_index = (self.first_index_in_Y + n_pages_between_bookmarks) % len(self.array_Y)
            self.array_Y[insert_index] = self.array_X[self.A]
            self.A -= 1

        elif m == 'B':  # Move from B to A
            page_front_of_B_index = (self.first_index_in_Y + n_pages_between_bookmarks - 1) % len(self.array_Y)
            self.A += 1
            self.array_X[self.A] = self.array_Y[page_front_of_B_index]

    def _is_bookmarks_placed(self):
        return self.A != -2 and self.B != -2
