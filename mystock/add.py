import datetime

from datareader.models import PeriodMinCnt2

end_point = [930216, 930727, 940729, 940913, 960119, 970512, 970923,
             980604, 980818, 981117, 990209, 990518, 990630,
             991227, '010613', '010824', '011022',
             '020122', '020625', '030103', '030416',
             '031113', '040407', '040628', '040913', '050120', '050603', '050711',  '050719',
             '071016', '081028', '090805',
             100415, 100705, 110418, 111021, 120106, 121203, 130218, 130625, 101204, 140228, 140721,
             150615, 150817, 151223, 160127, 160927, 161129, 170116, 170407, 170524, 171113, 171206, 180129, 180209, 180521, 180706, 180917, 180928]


start_point = ['1992-11-20', '1994-07-29', '1999-05-18', '2005-07-19', '2008-10-28', '2014-07-21']


for s in start_point:
    s = datetime.datetime.strptime(s, '%Y-%m-%d')

    for e in end_point:
        e = str(e)

        if e[0] == '9':
            e = '19' + e
        else:
            e = '20' + e

        e = datetime.datetime.strptime(e, '%Y%m%d')

        if s < e:
            print(s, e)

            o = PeriodMinCnt2()
            o.period_start = s
            o.period_end = e

            o.save()
