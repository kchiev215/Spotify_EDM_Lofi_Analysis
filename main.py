import track_extraction


def main(link):
    pl_URI = track_extraction.get_URI(link)
    track_extraction.get_track_info(pl_URI)


if __name__ == '__main__':
    main("37i9dQZF1DWWQRwui0ExPn")

