import random

def fifo(pags, num_frames):
    frames = []
    falta_de_pag = 0

    for pag in pags:
        if pag not in frames:
            if len(frames) < num_frames:
                frames.append(pag)
            else:
                frames.pop(0)
                frames.append(pag)
            falta_de_pag += 1

    return falta_de_pag


def lru(pags, num_frames):
    frames = []
    falta_de_pag = 0

    for pag in pags:
        if pag in frames:
            frames.remove(pag)
            frames.append(pag)
        else:
            if len(frames) < num_frames:
                frames.append(pag)
            else:
                frames.pop(0)
                frames.append(pag)
            falta_de_pag += 1

    return falta_de_pag


def gerarStringDeReferencia(length):
    return [random.randint(0, 9) for _ in range(length)]


def main():
    reference_string = gerarStringDeReferencia(50)
    num_frames_list = [2, 3, 4, 5]

    for num_frames in num_frames_list:
        fifo_faults = fifo(reference_string, num_frames)
        lru_faults = lru(reference_string, num_frames)

        print(f"Número de frames: {num_frames}")
        print(f"FIFO Falta de páginas: {fifo_faults}")
        print(f"LRU Falta de págibas: {lru_faults}")
        print()


if __name__ == "__main__":
    main()

