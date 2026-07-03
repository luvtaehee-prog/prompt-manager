CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 밝은 배경, 제품 중심 구도, 고급스러운 조명을 적용합니다.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "뉴스 요약 프롬프트",
        "content": "다음 뉴스 기사를 3문장으로 요약해주세요. 핵심 사실만 포함하고 주관적 해석은 제외합니다.",
        "category": "자동화",
        "favorite": False
    }
]
def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    title = input("제목: ").strip()
    while not title:
        title = input("제목을 입력하세요: ").strip()

    content = input("내용: ").strip()
    while not content:
        content = input("내용을 입력하세요: ").strip()

    print("\n카테고리 선택:")
    for i, c in enumerate(CATEGORIES, 1):
        print(f"{i}) {c}")
    sel = input("선택: ").strip()

    if sel.isdigit() and 1 <= int(sel) <= len(CATEGORIES):
        category = CATEGORIES[int(sel) - 1]
    else:
        category = sel if sel else "기타"

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print("\n프롬프트가 추가되었습니다!")


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            add_prompt()
        elif choice in ["2", "3", "4", "5", "6", "7"]:
            print(f"[{choice}번] 기능은 아직 구현되지 않았습니다.")
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")


if __name__ == "__main__":
    main()
