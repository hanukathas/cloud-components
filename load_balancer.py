from dataclasses import dataclass, field

import random



@dataclass
class LoadBalancer:
    server_pool: dict = field(default_factory=dict)
    server_picked_count: dict = field(default_factory=dict)


    def add_server(self, server_id: int) -> bool:
        try:
            if server_id not in self.server_pool:
                self.server_pool[server_id] = 'available'
            else:
                print(f"server id {server_id} is in pool already")
            return True
        except Exception as e:
            print(e.__class__)
            return False

    def remove_server(self, server_id: int) -> bool:
        try:
            if server_id in self.server_pool:
                self.server_pool.pop(server_id)
            return True
        except Exception as e:
            print(e.__class__)
            return False

    def pick_server(self):
        try:
            available_list = list()
            for k in self.server_pool.keys():
                if self.server_pool[k] == 'available':
                    available_list.append(k)
            print(available_list)
            picked = random.choice(available_list)
            self.picked_most(picked)
            print(f"randomly picked server:{picked}")
            self.server_pool[picked] = "picked"
            return picked

        except Exception:
            print(Exception.__class__)

    def release_server(self, server_id: int):
        try:
            if server_id in self.server_pool and self.server_pool[server_id] == 'picked':
                self.server_pool[server_id] = 'available'
                self.server_picked_count.pop(server_id)
        except Exception:
            print(Exception.__class__)

    def picked_most(self, server_id):
        if server_id in self.server_picked_count:
            self.server_picked_count[server_id] += 1
        else:
            self.server_picked_count[server_id] = 1
        return True

    def print_server_list(self):
        try:
            if len(self.server_pool) > 0:
                return self.server_pool
            else:
                return -1
        except Exception:
            print(Exception.__class__)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lb = LoadBalancer()
    lb.add_server(1)
    lb.add_server(2)
    lb.add_server(2)
    lb.add_server(3)
    lb.add_server(4)
    lb.add_server(5)
    print(f"current server list: {lb.print_server_list()}")
    print(f"picked server: {lb.pick_server()}")
    print(f"picked server: {lb.pick_server()}")
    print(f"picked server: {lb.pick_server()}")
    print(f"picked server: {lb.pick_server()}")
    print(f"picked server: {lb.pick_server()}")
    lb.release_server(1)
    lb.release_server(2)
    lb.release_server(3)
    print(f"picked server: {lb.pick_server()}")
    print(f"picked server: {lb.pick_server()}")
    print(f"picked count: {lb.server_picked_count}")
    print(f"current server list: {lb.print_server_list()}")



