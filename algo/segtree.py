def segfunc(x, y):
  # 最大を求める場合
  # return max(x, y)
  # 最小を求める場合
  # return min(x, y)
  # 区間和
  # return x + y
  # 区間積
  # return x * y
  # 最大公約数
  # return math.gcd(x, y)
  return

# 初期化
ide_ele = 
# 最小を求める場合
# ide_ele = float('inf')
# 最大を求める場合
# ide_ele = -float('inf')
# 区間和, 最大公約数
# ide_ele = 0
# 区間積
# ide_ele = 1


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res
