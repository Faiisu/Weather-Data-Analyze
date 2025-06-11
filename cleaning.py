import pandas as pd

def ProvinceClean(df: pd.DataFrame):
    ProvinceList = ['กระบี่', 'กรุงเทพมหานคร', 'กาญจนบุรี', 'กาฬสินธุ์', 'กำแพงเพชร',
       'ขอนแก่น', 'จันทบุรี', 'ฉะเชิงเทรา', 'ชลบุรี', 'ชัยนาท', 'ชัยภูมิ',
       'ชุมพร', 'ตรัง', 'ตราด', 'ตาก', 'นครนายก', 'นครปฐม', 'นครพนม',
       'นครราชสีมา', 'นครศรีธรรมราช', 'นครสวรรค์', 'นราธิวาส', 'น่าน',
       'บึงกาฬ', 'บุรีรัมย์', 'ปทุมธานี', 'ประจวบคีรีขันธ์', 'ปราจีนบุรี',
       'ปัตตานี', 'พระนครศรีอยุธยา', 'พะเยา', 'พังงา', 'พัทลุง', 'พิจิตร',
       'พิษณุโลก', 'ภูเก็ต', 'มหาสารคาม', 'มุกดาหาร', 'ยะลา', 'ยโสธร', 'ระนอง',
       'ระยอง', 'ราชบุรี', 'ร้อยเอ็ด', 'ลพบุรี', 'ลำปาง', 'ลำพูน', 'ศรีสะเกษ',
       'สกลนคร', 'สงขลา', 'สตูล', 'สมุทรปราการ', 'สมุทรสงคราม', 'สระแก้ว',
       'สุพรรณบุรี', 'สุราษฎร์ธานี', 'สุรินทร์', 'สุโขทัย', 'หนองคาย',
       'หนองบัวลำภู', 'อำนาจเจริญ', 'อุดรธานี', 'อุตรดิตถ์', 'อุทัยธานี',
       'อุบลราชธานี', 'เชียงราย', 'เชียงใหม่', 'เพชรบุรี', 'เพชรบูรณ์', 'เลย',
       'แพร่', 'แม่ฮ่องสอน']
    cleaned = df[df['Province'].isin(ProvinceList)].reset_index(drop=True)
    return cleaned

def WindDirecClean(df: pd.DataFrame):

    def check_wind(direc):
        if direc < 0 or direc > 360: return False
        return True

    df["WindDirecValid"] = df["WindDirection(degree)"].apply(check_wind)
    df = df[df['WindDirecValid'] == True]

    return df
    

def cleaningData(fileName):
    df = pd.read_parquet(fileName)
    for i in df: print(i)
    
    df = ProvinceClean(df)
    df = WindDirecClean(df)
    df.to_parquet("cleaned.parquet")

if __name__ == "__main__":
    cleaningData("format.parquet")