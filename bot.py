import zulip
import pprint
from ss import fn

pp = pprint.PrettyPrinter(indent=4)


class Bot():
    def __init__(self):
        self.client = zulip.Client(config_file="~/.zuliprc")
        self.subscribe()
        print("subscribed")

    def subscribe(self):
        stream_data = self.client.get_streams().get("streams")
        temp_dict = {}
        stream_list = []
        for data in stream_data:
            temp_dict["name"] = data.get("name")
            stream_list.append(temp_dict)

        result = self.client.add_subscriptions(stream_list)
        # pp.pprint(r)
        pp.pprint(stream_data)

    def process(self, msg):
        word = msg.get('content').lower().split(" ")
        print(word)
        # s = "Invalid command"
        words = ' '.join(word[1:])
        print(words)

        send_dict = {
            "type": "stream",
            "to": msg.get("display_recipient"),
            "subject": msg.get("subject"),
            "content": "Invalid command"   # <--- ismei doubt hai
        }

        fl = 0
        cmd_code = word[2]
        text_keys = ' '.join(word[3:])
        if cmd_code == "symptoms": 
            send_dict["content"] = fn(text_keys)
            result = self.client.send_message(send_dict)
            pp.pprint(result) 
        elif cmd_code == "disease": 
            send_dict["content"] = fn(text_keys)
            result = self.client.send_message(send_dict)
            pp.pprint(result) 
        elif cmd_code == "condition": 
            send_dict["content"] = fn(text_keys)
            result = self.client.send_message(send_dict)
            pp.pprint(result) 
        elif cmd_code == "risk": 
            send_dict["content"] = fn(text_keys)
            result = self.client.send_message(send_dict)
            pp.pprint(result) 
        elif cmd_code == "information": 
            send_dict["content"] = fn(text_keys)
            result = self.client.send_message(send_dict)
            pp.pprint(result)
        else:
            print("+++Err+++")
            result = self.client.send_message(send_dict)
        return


def main():
    bot = Bot()
    print("listening")
    bot.client.call_on_each_message(bot.process)


main()
