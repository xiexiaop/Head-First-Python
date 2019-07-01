import wave


path = "16k.wav"
with wave.open(path, "rb") as f:
    # print(f.getparams())
    frame = f.readframes(64)
    print(frame)

