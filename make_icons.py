"""Generate the home-screen icons (teal square with a white check mark). No dependencies."""
import struct
import zlib


def png(size, path):
    bg, fg = (15, 118, 110), (255, 255, 255)
    # check mark as two thick line segments, in unit coordinates
    segs = [((0.27, 0.52), (0.43, 0.68)), ((0.43, 0.68), (0.74, 0.34))]
    thick = 0.075

    def dist(px, py, a, b):
        (ax, ay), (bx, by) = a, b
        dx, dy = bx - ax, by - ay
        t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
        return ((px - ax - t * dx) ** 2 + (py - ay - t * dy) ** 2) ** 0.5

    rows = []
    for y in range(size):
        row = bytearray([0])
        for x in range(size):
            u, v = (x + 0.5) / size, (y + 0.5) / size
            d = min(dist(u, v, a, b) for a, b in segs)
            k = max(0.0, min(1.0, (thick - d) * size + 0.5))  # anti-aliased edge
            row += bytes(round(bg[i] + (fg[i] - bg[i]) * k) for i in range(3))
        rows.append(bytes(row))

    def chunk(t, data):
        c = t + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)

    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)))
        f.write(chunk(b"IDAT", zlib.compress(b"".join(rows), 9)))
        f.write(chunk(b"IEND", b""))


if __name__ == "__main__":
    png(180, "icon-180.png")
    png(512, "icon-512.png")
