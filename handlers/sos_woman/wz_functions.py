from loader import sdb


async def w_check_delete(answer, type_db, text=False, boshqa=False):
    if text:
        for n in type_db:
            if n[1] == answer:
                await sdb.delete_woman_text(text=answer)
    if boshqa:
        for n in type_db:
            if n[1] == answer:
                await sdb.delete_woman_unique(unique_id=answer)
