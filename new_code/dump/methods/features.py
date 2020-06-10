import new_code.dump.methods.crd as credential
import datetime


class Dustbin_Features:

    def auto_adjust(self, payload):
        self.value = int(payload) * 5 // 10

    def update_json(self, payload, topic):
        file_name = credential.json_data_files[topic]
        fp = open("new_code/dump/database/" + file_name, "w")
        print("{\n  filled: " + payload +
              ",\n  last_updated: " + str(datetime.datetime.now()) + " \n}", file=fp)

    def filled_percentage(self, payload, topic):
        if (self.value * 19 < int(payload)):
            self.update_json(self, "0", topic)
            print("0%")
        elif self.value * 18 < int(payload) <= self.value * 19:
            self.update_json(self, "5", topic)
            print("5%")
        elif self.value * 17 < int(payload) <= self.value * 18:
            self.update_json(self, "10", topic)
            print("10%")
        elif self.value * 16 < int(payload) <= self.value * 17:
            self.update_json(self, "15", topic)
            print("15%")
        elif self.value * 15 < int(payload) <= self.value * 16:
            self.update_json(self, "20", topic)
            print("20%")
        elif self.value * 14 < int(payload) <= self.value * 15:
            self.update_json(self, "25", topic)
            print("25%")
        elif self.value * 13 < int(payload) <= self.value * 14:
            self.update_json(self, "30", topic)
            print("30%")
        elif self.value * 12 < int(payload) <= self.value * 13:
            self.update_json(self, "35", topic)
            print("35%")
        elif self.value * 11 < int(payload) <= self.value * 12:
            self.update_json(self, "40", topic)
            print("40%")
        elif self.value * 10 < int(payload) <= self.value * 11:
            self.update_json(self, "45", topic)
            print("45%")
        elif self.value * 9 < int(payload) <= self.value * 10:
            self.update_json(self, "50", topic)
            print("50%")
        elif self.value * 8 < int(payload) <= self.value * 9:
            self.update_json(self, "55", topic)
            print("55%")
        elif self.value * 7 < int(payload) <= self.value * 8:
            self.update_json(self, "60", topic)
            print("60%")
        elif self.value * 6 < int(payload) <= self.value * 7:
            self.update_json(self, "65", topic)
            print("65%")
        elif self.value * 5 < int(payload) <= self.value * 6:
            self.update_json(self, "70", topic)
            print("70%")
        elif self.value * 4 < int(payload) <= self.value * 5:
            self.update_json(self, "75", topic)
            print("75%")
        elif self.value * 3 < int(payload) <= self.value * 4:
            self.update_json(self, "80", topic)
            print("80%")
        elif self.value * 2 < int(payload) <= self.value * 3:
            self.update_json(self, "85", topic)
            print("85%")
        elif self.value * 1 < int(payload) <= self.value * 2:
            self.update_json(self, "90", topic)
            print("90%")
        elif (int(payload) <= self.value * 1):
            self.update_json(self, "100", topic)
            print("100%")

        else:
            print("Invalid Value" + payload)
