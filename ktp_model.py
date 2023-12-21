import json


class KTPModel:
    def __init__(self, nik, nama, tempat_lahir, tgl_lahir, jenis_kelamin, gol_darah, alamat, agama, status_perkawinan,
                 pekerjaan, kewarganegaraan):
        self.nik = nik
        self.nama = nama
        self.tempat_lahir = tempat_lahir
        self.tgl_lahir = tgl_lahir
        self.jenis_kelamin = jenis_kelamin
        self.gol_darah = gol_darah
        self.alamat = alamat
        self.agama = agama
        self.status_perkawinan = status_perkawinan
        self.pekerjaan = pekerjaan
        self.kewarganegaraan = kewarganegaraan

    def toJson(self):
        return json.dumps(self.__dict__)

    @classmethod
    def fromJson(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
