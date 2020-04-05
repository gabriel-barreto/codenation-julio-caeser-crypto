import argparse
import json

import decryption
import hash


def update_payload(file: str, payload: dict) -> bool:
    with open(file, 'w', encoding='UTF-8') as json_file:
        json_file.write(json.dumps(payload, indent=4))
        json_file.close()
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="main.py")

    # ==> Arguments
    parser.add_argument(
        "file",
        help="JSON file path with payload",
        type=str,
        metavar="[JSON PAYLOAD FILE PATH]"
    )

    args = parser.parse_args()

    with open(args.file, 'r', encoding='UTF-8') as json_file:
        payload = json.loads(json_file.read())
        json_file.close()

    d = decryption.decrypt(payload['cifrado'], payload['numero_casas'])
    h = hash.gen(d)

    payload['decifrado'] = d
    payload['resumo_criptografico'] = h
    update_payload(args.file, payload)
