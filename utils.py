class AverageMeter(object):
    """From https://github.com/pytorch/examples/blob/master/imagenet/main.py"""

    def __init__(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def __repr__(self):
        return f'{self.avg:.2e}'

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


class dotdict(dict):
    def __getattr__(self, name):
        return self[name]    # 妙啊，把字典的key变成了attribute，不过对于key是字符串来说，就有点丑陋了，大概
        # 字符串不会丑陋的，因为会自动转化过去，太神奇了，不懂为什么会这样 比如说你有个key是‘alpha’，那普通的字典查看值就要dict['alpha']，但是用了dotdict之后，就可以直接dict.alpha
