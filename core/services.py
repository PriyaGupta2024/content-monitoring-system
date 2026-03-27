def calculate_score(keyword, content):
    keyword_lower = keyword.lower()
    title = content.title.lower()
    body = content.body.lower()

    if keyword_lower in title:
        return 100
    elif keyword_lower in title:
        return 70
    elif keyword_lower in body:
        return 40
    return 0


def should_create_flag(keyword, content):
    existing_flag = Flag.objects.filter(
        keyword=keyword,
        content_item=content
    ).first()

    if existing_flag:
        # if marked irrelevant and content not changed → skip
        if (existing_flag.status == 'irrelevant' and
            existing_flag.content_item.last_updated == content.last_updated):
            return False

    return True