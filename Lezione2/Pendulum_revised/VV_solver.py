class VV_solver:
    def __init__(self, F, tau):
        self.F = F
        self.tau = tau

    def solve(self, N : int, x0, v0):
        x = [x0]
        v = [v0]
        time = [0]
        for i in range(N):
            newX, newV = self.step(x[i], v[i])
            x.append(newX)
            v.append(newV)
            time.append(time[i] + self.tau)
        return time, x, v

    def step(self, x, v):
        return self.updateX(x, v), self.updateV(x, v)

    def updateX(self, x, v):
        return x + v * self.tau + self.F(x) * self.tau**2 /2

    def updateV(self, x, v):
        return v + self.tau * (self.F(x) + self.F(self.updateX(x, v))) / 2
