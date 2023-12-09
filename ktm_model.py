import json


class KTMModel:
    def __init__(self, nim, nama, ttl, jurusan, alamat):
        self.nim = nim
        self.nama = nama
        self.ttl = ttl
        self.jurusan = jurusan
        self.alamat = alamat

    def toJson(self):
        return json.dumps(self.__dict__)

    @classmethod
    def fromJson(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
