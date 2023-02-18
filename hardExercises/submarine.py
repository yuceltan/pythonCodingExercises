class submarine:
    def init(self,name,depth=0):
        self.name=name
        self.depth=depth

    def ascend(self,x3):
        if self.depth+x3>0:
            print('you are a submarine, you can not go further above the sea level!')
        else:
            self.depth=self.depth+x3
    def descend(self,x4):
        self.depth=self.depth-x4

    def check_depth(self):
        print(f'your currrent depth is: {self.depth}')