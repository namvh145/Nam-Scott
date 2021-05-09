import time

import scrapy


class Expert(scrapy.Spider):
    name = "Nguyen"
    start_urls = [
        "https://www.researchgate.net/search/researcher?q=nguyen"
    ]

    list_name = ['nguyen', 'thi', 'le', 'hoang', 'ngoc', 'anh', 'minh', 'pham', 'thanh', 'huynh', 'dang', 'dinh', 'bui', 'do', 'ha', 'phuong', 'tran', 'duong', 'hong', 'duc', 'kim', 'phan', 'mai', 'linh', 'my', 'duy', 'ho', 'ngo', 'doan', 'bao', 'khanh', 'thuy', 'lam', 'dao', 'huy', 'hai', 'ly', 'hung', 'cong', 'cao', 'huu', 'nhu', 'quang', 'huong', 'luong', 'an', 'dung', 'chi', 'thao', 'kieu', 'chau', 'thu', 'nhi', 'hoa', 'nhat', 'quynh', 'gia', 'huyen', 'hieu', 'giang', 'quoc', 'hien', 'luu', 'bich', 'hoai', 'ngan', 'phung', 'nam', 'lan', 'van', 'thai', 'binh', 'long', 'dat', 'truong', 'chu', 'cuong', 'cam', 'dieu', 'manh', 'phuc', 'hang', 'ba', 'hanh', 'thien', 'dong', 'tien', 'hao', 'diem', 'nhan', 'tan', 'trinh', 'duyen', 'son', 'phu', 'han', 'ta', 'tam', 'bach', 'hue', 'nga', 'diep', 'khoa', 'quyen', 'dai', 'phuoc', 'phong', 'nghia', 'khang', 'loc', 'quan', 'lai', 'phi', 'loan', 'dam', 'nie', 'nong', 'quach', 'hau', 'kien', 'nhung', 'nguyet', 'tuan', 'hiep', 'the', 'tu', 'la', 'dan', 'danh', 'thang', 'chung', 'tai', 'ai', 'oanh', 'khoi', 'phat', 'lien', 'khac', 'sang', 'ky', 'khai', 'chinh', 'trang', 'ma', 'du', 'to', 'kha', 'hoan', 'quy', 'tuong', 'trung', 'chien', 'hua', 'luan', 'trong', 'toan', 'man', 'nha', 'trieu', 'bang', 'mong', 'dac', 'loi', 'eban', 'luc', 'kiet', 'nu', 'nghiem', 'thinh', 'nghi', 'vu', 'khuong', 'truc', 'khuat', 'thuan', 'ninh', 'tram', 'lieu', 'nhut', 'lu', 'can', 'dien', 'vo', 'thuong', 'tang', 'bya', 'thuc', 'canh', 'be', 'mlo', 'chuong', 'que', 'tri', 'thach', 'tinh', 'lo', 'huan', 'uyen', 'ban', 'thong', 'tuyet', 'viet', 'ayun', 'tham', 'tung', 'cat', 'chan', 'sy', 'chanh', 'cuc', 'mi', 'tuyen', 'tin', 'dau', 'tho', 'than', 'au', 'bac', 'suong', 'boi', 'thy', 'lang', 'khiem', 'tra', 'bien', 'tong', 'buu', 'lap', 'luyen', 'quyet', 'lanh', 'giao', 'si', 'sam', 'vinh', 'sinh', 'qui', 'khue', 'liem', 'hop', 'vi', 'giau', 'nhien', 'doanh', 'tat', 'cu', 'hy', 'ton', 'di', 'chuc', 'mac', 'chieu', 'khuyen', 'khong', 'hoi', 'adrong', 'tieu', 'na', 'da', 'vy', 'co', 'cham', 'buon', 'bkrong', 'song', 'thieu', 'kbuor', 'giap', 'ngoan', 'em', 'knul', 'banh', 'chuyen', 'mau', 'ca', 'thoai', 'duoc', 'hoc', 'cung', 'lac', 'mo', 'men', 'de', 'nang', 'that', 'ni', 'khuu', 'che', 'don', 'may', 'khuc', 'kiem', 'enuol', 'su', 'ksor', 'nho', 'sung', 'san', 'nham', 'sa', 'kinh', 'chang', 'mao', 'luat', 'vuong', 'khiet', 'nghiep', 'sen', 'tao', 'nuong', 'diu', 'doi', 'bo', 'hmok', 'ngu', 'gam', 'muoi', 'duan', 'thoi', 'thoa', 'hwing', 'kdam', 'lich', 'hinh', 'mach', 'tay', 'nhon', 'lieng', 'ong', 'ny', 'mung', 'on', 'ktla', 'ben', 'lua', 'mui', 'chiem', 'sao', 'cai', 'bay', 'hoanh', 'phap', 'tiep', 'pho', 'ke', 'duyet', 'len', 'ngat', 'nhuong', 'nay', 'krong', 'ngon', 'ich', 'hon', 'lau', 'bong', 'ty', 'cau', 'thiet', 'gioi', 'thuyen', 'them', 'no', 'bon', 'pha', 'mien', 'lao', 'seo', 'kpa', 'ro', 'oai', 'so', 'toi', 'nhuan', 'cap', 'bdap', 'pang', 'hlong', 'nguy', 'li', 'niem', 'sau', 'khau', 'ka', 'hdok', 'gai', 'bau', 'ut', 'hoat', 'uy', 'xuan', 'mua', 'uong', 'moc', 'sai', 'thom', 'chuan', 'nien', 'sanh', 'tue', 'thuat', 'nghe', 'kdoh', 'lin', 'dep', 'cang', 'me', 'luy', 'cuu', 'hot', 'khieu', 'sieu', 'ket', 'din', 'thiem', 'tha', 'phoi', 'leng', 'nhieu', 'nhai', 'noi', 'soan', 'vien', 'chin', 'ung', 'lenh', 'den', 'bi', 'nen', 'dua', 'chon', 'hap', 'bin', 'thuyet', 'kham', 'cha', 'thiep', 'chong', 'bieu', 'lim', 'truyen', 'tanh', 'dap', 'gian', 'hen', 'theu', 'moi', 'con', 'sac', 'day', 'dak', 'arul', 'liu', 'he', 'giai', 'trien', 'khe', 'mon', 'sim', 'nhanh', 'bun', 'dich', 'cac', 'tuoi', 'hac', 'lung', 'bat', 'ham', 'muon', 'lynh', 'mang', 'alio', 'kpor', 'ngai', 'kong', 'toai', 'khen', 'khan', 'phang', 'triet', 'khoe', 'khoan', 'nhac', 'chiu', 'phien', 'trac', 'doai', 'hra', 'hi', 'ri', 'krieng', 'kman', 'sruk', 'kuan', 'vang', 'but', 'thua', 'tiet', 'chat', 'det', 'nhiem', 'thoang', 'phai', 'te', 'cho', 'bot', 'tot', 'diet', 'tich', 'dim', 'due', 'en', 'hoac', 'luk', 'dok', 'ne', 'ra', 'ding', 'min', 'khon', 'cua', 'thon', 'rin', 'leo', 'leu', 'thac', 'thich', 'tru', 'lon', 'ngoi', 'chen', 'tac', 'in', 'cil', 'ngot', 'gip', 'kon', 'ecam', 'ghi', 'hoe', 'nh', 'suu', 'tap', 'lay', 'kam', 'luom', 'lee', 'chap', 'trai', 'ktul', 'chay', 'senh', 'phay', 'boc', 'bua', 'nguon', 'phon', 'hay', 'luon', 'phao', 'chenh', 'chieng', 'thin', 'choi', 'deo', 'diec', 'hat', 'gieng', 'gin', 'buoi', 'rcam', 'hdrue', 'dy', 'teh', 'lia', 'apuot', 'quoi', 'teo', 'thoan', 'nhang', 'nim', 'siu', 'tsan', 'rim', 'ang', 'ao', 'sua', 'khu', 'eng', 'nghien', 'nui', 'bai', 'sep', 'tuc', 'tuy', 'heng', 'phe', 'cun', 'nhinh', 'kiu', 'am', 'giam', 'net', 'guong', 'goi', 'bil', 'del', 'dem', 'duen', 'ga', 'jin', 'ju', 'juan', 'mdrang', 'mun', 'sum', 'phieu', 'huang', 'ko', 'chia', 'kin', 'at', 'nhin', 'mieu', 'ngac', 'thuoc', 'sin', 'quat', 'thap', 'quanh', 'ti', 'pen', 'vong', 'xa', 'ndu', 'sun', 'cach', 'hiem', 'nghin', 'xanh', 'pi', 'suc', 'cay', 'khoat', 'rac', 're', 'vui', 'muu', 'chua', 'bieng', 'bion', 'eung', 'duom', 'brit', 'hun', 'je', 'liep', 'lip', 'ken', 'sia', 'bam', 'beo', 'bia', 'lem', 'sieng', 'moan', 'buoc', 'nin', 'mok', 'rya', 'muc', 'bung', 'thieng', 'qua', 'dia', 'hu', 'khoang', 'bol', 'nhuyen', 'mot', 'rong', 'thau', 'khao', 'then', 'ghen', 'phin', 'ron', 'se', 'tau', 'tenh', 'set', 'jrang', 'niekdam', 'ja', 'jem', 'ting', 'suin', 'thuel', 'truk', 'ya', 'nhay', 'pu', 'khuy', 'khuyn', 'noan', 'ru', 'nganh', 'duon', 'inh', 'khot', 'tiem', 'soi', 'suat', 'chac', 'chao', 'cheng', 'nhip', 'nghinh', 'tro', 'alen', 'go', 'ria', 'nung', 'dip', 'rieu', 'khuynh', 'khien', 'kia', 'ry', 'gan', 'dah', 'fa', 'ching', 'pao', 'gua', 'khoai', 'gien', 'drue', 'bera', 'bhen', 'bip', 'bit', 'blim', 'blin', 'bu', 'cel', 'chel', 'adat', 'cieu', 'der', 'dik', 'djin', 'djuan', 'bhok', 'drim', 'duin', 'duyn', 'gau', 'get', 'goa', 'gu', 'hieng', 'im', 'jan', 'jo', 'jun', 'kheo', 'drao', 'lina', 'luyt', 'meo', 'mila', 'miu', 'mri', 'nguan', 'nguet', 'jri', 'kjie', 'mjao', 'pri', 'pe', 'bim', 'blo', 'dar', 'doen', 'dri', 'duo', 'dup', 'el', 'eo', 'gue', 'guen', 'hiu', 'joi', 'juel', 'juin', 'drong', 'mak', 'nao', 'nel', 'ngam', 'nis', 'rai', 'bto', 'nuol', 'rcom', 'hach', 'hia', 'ng', 'ril', 'tren', 'huyet', 'saly', 'thay', 'sor', 'kao', 'uan', 'eun', 'thuk', 'khi', 'soat', 'khuon', 'xinh', 'diana', 'tieng', 'lop', 'phiet', 'giac', 'triu', 'hyun', 'nhe', 'nuoc', 'lui', 'hin', 'trach', 'tuu', 'aly', 'mu', 'ayua', 'khinh', 'ngung', 'nguuyen', 'fu', 'dara', 'mary', 'nhuc', 'pil', 'hiet', 'nhun', 'phet', 'luynh', 'gon', 'doat', 'soai', 'sot', 'troi', 'truoc', 'theo', 'phun', 'rah', 'mah', 'ronik', 'khin', 'liang', 'liet', 'tchen', 'phol', 'jam', 'nut', 'ray', 'thoong', 'nuoi', 'nai', 'uoc', 'phich', 'nua', 'say', 'dieng', 've', 'wang', 'won', 'top', 'kop', 'bom', 'bron', 'gun', 'dun', 'tor', 'sur', 'nom', 'jamin', 'bjrang', 'thio', 'ntor', 'niel', 'oan', 'triek', 'ran', 'sel', 'sion', 'tit', 'tuyn', 'win', 'wuong', 'arun', 'ntrual', 'ahmad', 'pin', 'valerie', 'aydob', 'aysah', 'tuoc', 'bnuoch', 'bubakar', 'khim', 'rat', 'tre', 'uom', '96', 'caothi', 'chaneyarbane', 'hsiang', 'meng', 'hasir', 'chheang', 'chou', 'hsiung', 'chuang', 'cody', 'jackson', 'cut', 'brice', 'guot', 'daichi', 'nhim', 'lily', 'dech', 'bet', 'bou', 'nguynh', 'kenh', 'muan', 'nhiet', 'henh', 'nhy', 'hich', 'tseng', 'ngun', 'tuat', 'doduc', 'bireer', 'soni', 'duu', 'fan', 'fati', 'featherstone', 'jack', 'francis', 'plau', 'gion', 'giuong', 'girih', 'gosain', 'ravi', 'alei', 'bru', 'chuhy', 'djuen', 'kieng', 'dola', 'alech', 'aron', 'biak', 'bic', 'bih', 'blak', 'blem', 'blep', 'bliak', 'bloan', 'blon', 'bluon', 'boan', 'bop', 'bor', 'bren', 'breny', 'bret', 'brin', 'cen', 'deng', 'dier', 'djuah', 'djuic', 'djuin', 'dlan', 'doa', 'drai', 'dream', 'drum', 'duien', 'emilie', 'es', 'estes', 'gen', 'gim', 'gloai', 'gok', 'hoam', 'hoch', 'hui', 'ien', 'jer', 'jit', 'joach', 'joar', 'juyn', 'kac', 'kala', 'katherin', 'kep', 'klim', 'kluc', 'koh', 'lany', 'mla', 'kdue', 'liza', 'luet', 'lum', 'lysa', 'mari', 'milka', 'mir', 'misi', 'mlam', 'mol', 'muin', 'mulo', 'nac', 'nera', 'ngiep', 'ngim', 'nhel', 'nhoa', 'nhoan', 'nhuh', 'nan', 'sil', 'siva', 'phra', 'mkang', 'dakcat', 'bja', 'taih', 'djoan', 'lom', 'duah', 'jah', 'june', 'agi', 'andri', 'bak', 'bel', 'bena', 'bep', 'bhan', 'bhenh', 'bhit', 'bier', 'blac', 'blen', 'bleng', 'blia', 'bluen', 'bluin', 'bluk', 'blunh', 'bri', 'buc', 'buel', 'buih', 'chiar', 'choat', 'chuon', 'chuot', 'cuel', 'dala', 'debora', 'debura', 'dian', 'diang', 'dina', 'dir', 'djuat', 'dli', 'dlu', 'doang', 'byang', 'dolin', 'dram', 'druen', 'duer', 'dum', 'elisabets', 'eni', 'et', 'gem', 'gier', 'glat', 'glin', 'goai', 'guain', 'guan', 'guon', 'helibia', 'hieo', 'huien', 'janet', 'jier', 'juk', 'july', 'juon', 'eya', 'kabi', 'kal', 'kamira', 'kayun', 'kem', 'kol', 'kru', 'kuin', 'lari', 'liam', 'lida', 'lion', 'loanh', 'loet', 'luen', 'luin', 'mar', 'mat', 'mil', 'miong', 'mlin', 'babi', 'mron', 'myun', 'ngin', 'ngoat', 'hrue', 'nhen', 'nheo', 'nhiu', 'nhuol', 'noen', 'nia', 'riang', 'rom', 'kiel', 'com', 'toanh', 'nul', 'zin', 'ak', 'bli', 'dorit', 'lic', 'lisa', 'thiec', 'pieng', 'gwendoline', 'cheung', 'far', 'kholisgoh', 'phau', 'phot', 'uc', 'chun', 'tzu', 'huc', 'christophe', 'bup', 'ngay', 'jacky', 'low', 'jennifer', 'arata', 'kee', 'sing', 'quay', 'khuou', 'tae', 'shichi', 'jong', 'kra', 'noba', 'mam', 'huat', 'nhoc', 'xai', 'xia', 'benl', 'lila', 'linl', 'timothy', 'country', 'great', 'chheng', 'decho', 'khar', 'fang', 'loakhajorn', 'nhap', 'rang', 'thuu', 'yen', 'schang', 'da0', 'mnh', 'gio', 'kinam', 'hamzah', 'lachor', 'marona', 'mguyen', 'aziz', 'mad', 'amru', 'adam', 'harofat', 'alinda', 'broch', 'lyca', 'veh', 'chuen', 'ngguyen', 'bech', 'sach', 'rot', 'doc', 'giay', 'daniela', 'chuom', 'gioan', 'ewelina', 'fernandez', 'miccah', 'th', 'nghuyet', 'huot', 'nghy', 'kristin', 'mohamad', 'myn', 'nghenh', 'dzi', 'bouvier', 'dzung', 'by', 'nhue', 'ruc', 'hynh', 'nau', 'ngao', 'phiem', 'niu', 'non', 'phim', 'sien', 'soal', 'edwards', 'ruong', 'jim', 'keo', 'kiep', 'mem', 'riu', 'thia', 'tiu', 'tol', 'vung', 'aminah', 'guy', 'enny', 'hly', 'ieu', 'tem', 'ji', 'oh', 'ok', 'osaki', 'anwar', 'chio', 'christopher', 'ayob', 'dally', 'coi', 'misa', 'ral', 'giu', 'kelly', 'gina', 'nhot', 'duoi', 'phing', 'nuu', 'ruou', 'pur', 'phuy', 'po', 'puih', 'jony', 'mas', 'rec', 'reyes', 'kathy', 'rmah', 'fi', 'lick', 'kuen', 'aybar', 'carmona', 'ki', 'nah', 'hozen', 'phui', 'salaymang', 'keun', 'saphy', 'banam', 'piotr', 'hogo', 'mina', 'gay', 'ming', 'jeong', 'bhatia', 'sison', 'som', 'alex', 'sonny', 'denh', 'sui', 'onl', 'phua', 'takahara', 'koon', 'tchang', 'tchuong', 'teck', 'rinh', 'rogers', 'va', 'onphen', 'bra', 'brai', 'brem', 'dot', 'het', 'klinh', 'neo', 'nhuot', 'peu', 'mit', 'sari', 'soc', 'muop', 'hermanson', 'iris', 'gi', 'kuroda', 'tom', 'tony', 'syn', 'anna', 'duly', 'nhuy', 'duat', 'chiec', 'til', 'ngocthang', 'pascal', 'pon', 'col', 'luot', 'riem', 'cop', 'huyn', 'nghieu', 'quen', 'riep', 'suot', 'trat', 'cuoi', 'trau', 'nhuoc', 'nhoi', 'ngocthien', 'lyn', 'vay', 'tsoi', 'akbar', 'hajireen', 'kummis', 'hassan', 'kip', 'ligia', 'quyt', 'khiao', 'reo', 'rem', 'ven', 'khia', 'biet', 'soa', 'khach', 'crum', 'roi', 'voong', 'nina', 'dzu', 'chuy', 'toa', 'vuu', 'wen', 'changhee', 'tim', 'chai', 'aram', 'kuak', 'mal', 'muen', 'nip', 'pas', 'sonik', 'tach', 'tror', 'wach', 'bec', 'bhot', 'bok', 'boy', 'cep', 'kso', 'ciu', 'cot', 'cuen', 'cuk', 'cum', 'cuor', 'wik', 'dambi', 'davit', 'dawid', 'dhin', 'nar', 'kbin', 'dj', 'har', 'drin', 'druynh', 'duet', 'dui', 'duna', 'knia', 'ero', 'fen', 'fruit', 'gham', 'ghau', 'gir', 'glay', 'goang', 'gol', 'goong', 'goul', 'grat', 'grik', 'gron', 'guel', 'gui', 'hem', 'heni', 'henri', 'her', 'hing', 'huen', 'huon', 'hur', 'mbuon', 'jaly', 'jaran', 'mya', 'jari', 'jean', 'jek', 'jerome', 'jiem', 'jieu', 'jing', 'jio', 'johnny', 'josia', 'judo', 'jul', 'kaben', 'kador', 'kai', 'kaih', 'kaip', 'kaisa', 'kalep', 'kaly', 'kar', 'kat', 'khel', 'khem', 'khewin', 'khiep', 'khing', 'khiu', 'khua', 'khuan', 'klam', 'klep', 'kler', 'klin', 'krec', 'krul', 'ku', 'kung', 'kuong', 'kuyn', 'ling', 'luai', 'ludo', 'luit', 'fata', 'markos', 'mic', 'mich', 'mida', 'mik', 'milo', 'mip', 'muel', 'muser', 'mut', 'nak', 'ner', 'ngap', 'ngenh', 'ngher', 'ngia', 'ngoa', 'nhao', 'nigo', 'nikol', 'noang', 'noel', 'not', 'nue', 'nuen', 'nuk', 'or', 'ora', 'owen', 'pan', 'phel', 'phem', 'phen', 'philimon', 'philip', 'rluk', 'phiol', 'phit', 'phoa', 'piong', 'pol', 'pot', 'prao', 'prem', 'priu', 'pruet', 'trei', 'ram', 'rap', 'reu', 'rgei', 'ric', 'rika', 'ringo', 'robi', 'rova', 'ruin', 'rum', 'rumy', 'runa', 'rung', 'sacty', 'saka', 'samak', 'drea', 'sekin', 'seng', 'siek', 'sier', 'silaih', 'simon', 'soen', 'sol', 'hrah', 'steven', 'sue', 'suel', 'suet', 'suk', 'suoi', 'suon', 'suor', 'niesieng', 'amlo', 'nieksieng', 'thani', 'thip', 'thot', 'ning', 'thun', 'thuo', 'hdrai', 'ksa', 'tlep', 'toang', 'tros', 'ryam', 'tuen', 'tuih', 'tuin', 'tuynh', 'ui', 'uri', 'vansi', 'vit', 'vuih', 'vuot', 'wan', 'wi', 'wim', 'woi', 'wol', 'wuk', 'xem', 'xiam', 'nas', 'aroh', 'jery', 'koni', 'amot', 'mision', 'nguai', 'pam', 'dhar', 'bluh', 'dhiu', 'dic', 'huol', 'nieng', 'saetia', 'pac', 'yu']

    def parse(self, response, **kwargs):
        for i in range(200):
            original_link = response.url.split("=")[0] + "=" + self.list_name[i]
            yield scrapy.Request(original_link + "&page=1", callback=self.parse_link)


    def parse_link(self, response, **kwargs):
        time.sleep(5)
        experts_link = response.css(".nova-v-person-item__title .nova-e-link--theme-bare::attr(href)").extract()
        for link in experts_link:
            yield scrapy.Request("https://www.researchgate.net/" + link, callback=self.parseName)
        nextpage = str(response.url).split('&')[0]
        nnext = int(response.url.split('&')[1].split('=')[1]) + 1
        if nnext < 15:
            yield scrapy.Request(nextpage + '&page=' + str(nnext), callback=self.parse_link)

    def parseName(self, response):
        time.sleep(5)
        skills = []
        skills = response.css('.nova-l-flex__item .nova-e-badge::text').extract()
        name = response.css('.nova-o-grid__column .nova-e-text::text').extract()[0]
        infos = response.css("div[class='nova-e-text nova-e-text--size-xl nova-e-text--family-sans-serif nova-e-text--spacing-none nova-e-text--color-inherit']::text").extract()

        try:
            school_address = '.nova-e-link .nova-e-text span::text'
            school = response.css(school_address).extract()[0]
        except:
            school = None
        try:
            publications = int(infos[0])
        except:
            publications = 0
        try:
            citations = int(infos[2])
        except:
            citations = 0
        description = None
        elements = response.css('.Linkify::text').extract()
        if len(elements) > 0:
            description = ""
        for e in elements:
            description += e
        yield {
            "name": name,
            "school": school,
            "publications": publications,
            "citations": citations,
            "description": description,
            "skills": skills
        }