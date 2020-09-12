import crawlingw
import crawlingn
import crawlinge

def main():
    while(True):
        print('키워드를 입력하세요: ', end='')
        put = input()
        if put == '0':
            break
        
        # res = []
        # res.append(crawlingn.crawler(put))    # 네이버 백과 크롤링 (비슷한 키워드 반환)
        # res.append(crawlingw.crawler(put))    # 위키백과(한글) 크롤링 (분류 반환)
        # res.append(crawlinge.crawler(put))    # 위키백과(영어) 크롤링 (분류 반환)
        # 위키백과(영어) 부분은 동음이의어 부분 제대로 구현 못해놔서 크롤링이 잘 안됩니다 ㅜㅜ

        res = []
        if False:   # 이부분은 검색어를 카테고리로 분류한 다음 카테고리와 비슷한 키워드를 반환
            temp = crawlingw.crawler(put)
            if not temp:
                continue
            res = temp[:]
            for i in temp:
                res.extend(crawlingn.crawler(i))
        if True:   # 이부분은 검색어의 비슷한 키워드 따로,  분류 따로 크롤링해서 반환
            res.append(crawlingn.crawler(put))
            res.append(crawlingw.crawler(put))
            res.append(crawlinge.crawler(put))
        
        if res:
            print(f'결과 = {res}')
        else:
            print('키워드를 찾을 수 없어요..')

if __name__ == '__main__':
    main()