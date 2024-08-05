from cryptofuzz import Convertor

conv = Convertor()


class Wallet:
    def PrivateKey_To_Address(self, privatekey: str, compress=False) -> str:
        if compress:
            return conv.hex_to_addr(privatekey, compress=True)
        else:
            return conv.hex_to_addr(privatekey, compress=False)



