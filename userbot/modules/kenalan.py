from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.i(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Hai, Kenalin, Namaku NCHAN`")
    sleep(3)
    await typew.edit("20 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di Jawa Timur, Salam Kenal Yak:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.syg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Mau ngasih tau, kalau...`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`Love You Byy 😘😘😘`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.smgt(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Hidup, Bermanfaat Untuk Sesama`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart
