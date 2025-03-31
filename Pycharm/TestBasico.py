import random
import unittest
import json

from Pycharm.ServidorCache import ServidorCache
from Pycharm.ServidorMaestro import ServidorMaestro
from Pycharm.Video import Video
from Pycharm.key_sort import key_sort


def carga_dataset(data):
    with open(data) as f:
        test_datasets = json.load(f)

    videos = list()
    for v in test_datasets["videos"]:
        v_obj = Video(v["name"], v["size"], v["fee"])
        for c, u in v["users"].items():
            v_obj.set_users(c, u)
        videos.append(v_obj)

    servers = dict()
    for s in test_datasets["servers"]:
        servers[s["country"]] = ServidorCache(s["identifier"], s["country"], s["size"])

    pings = test_datasets["pings"]
    p_ = dict()
    for s in servers.values():
        p_[s] = dict()
        for p in pings[s.country]:
            p_[s][servers[p]] = pings[s.country][p]
    maestro = ServidorMaestro(servers.values(), p_)

    return videos, servers, maestro

class TestBasico(unittest.TestCase):

    def test_carga_simple(self):
        datos = [random.randint(0, 100) for _ in range(100)]
        ordenados = sorted(datos)
        key_sort(datos)
        self.assertEqual(ordenados, datos)

        v, s, m = carga_dataset("toy.json")

        spain = s["Spain"]
        spain.rellena(v)
        self.assertEqual(spain.tiempo_emision(), 578000)
        almacenados = spain.almacenados()
        self.assertIn((v[3], 0.5), almacenados)

        m.simplifica_grafo()
        self.assertEqual(m.mas_cercano(s["Spain"]), s["France"])
        m.simplifica_grafo()
        self.assertEqual(m.mas_cercano(s["Spain"]), s["France"])
        self.assertEqual(m.mas_cercano(s["France"]), s["Spain"])


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)