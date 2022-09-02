import Authorization
import track_extraction
import database


# EDM hits
EDM_PL = "37i9dQZF1DX1kCIzMYtzum"
EDM_HITS = "37i9dQZF1DX3Kdv0IChEm9"
LOFI_BEATS = "37i9dQZF1DWWQRwui0ExPn"

def main_LoFi(link):
    pl_URI = track_extraction.get_URI(link)
    track_df = track_extraction.get_track_info(pl_URI)
    database.create_load_LoFi()
    database.insert_data_Lofi(track_df)

def main_EDM(link):
    pl_URI = track_extraction.get_URI(link)
    track_df = track_extraction.get_track_info(pl_URI)
    database.create_load_EDM()
    database.insert_data_EDM(track_df)

if __name__ == '__main__':

    main_LoFi("37i9dQZF1DWWQRwui0ExPn")