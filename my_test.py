import logging


class Logutil:
    def __init__(self):
        self.log = logging.getLogger("坤坤")
        self.log.setLevel(logging.INFO)
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)
        sh.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        fh = logging.FileHandler("zzc.log", "a", encoding="utf-8")
        fh.setLevel(logging.WARNING)
        fh.setFormatter(logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s"))
        fh.close()
        self.log.addHandler(sh)
        self.log.addHandler(fh)

