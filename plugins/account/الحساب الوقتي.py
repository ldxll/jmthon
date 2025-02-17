"""

❃ `{i}ساعة جنب الاسم`
   لـ بدأ وضع الساعة مع اسمك حسابك

❃ `{i}انهاء الساعة`
   لـ تعطيل ظهور الساعة مع الأسم الخاص بك

❃ `{i}الساعة بالبايو`
   لـ بدأ وضع الساعة مع النبذة/البايو الخاص بك

❃ `{i}انهاء ساعة البايو`
   لـ تعطيل ظهور الوقت مع النبذة الخاصة بك
"""

import asyncio
import random
import time

from telethon.tl.functions.account import UpdateProfileRequest

from .. import JmdB, jmubot, jmthon_cmd

USERBIO = JmdB.get_key("isco") or "إذا ما مشت قدماي فوق ترابهم ، ظنوهُ تاجًا فوقَ هامِ جبينِهِم"
NAME = JmdB.get_key("NAME")


@jmthon_cmd(pattern="اسم وقتي$")
async def autoname(event):
    if JmdB.get_key("AUTONAME"):
        return await event.eor("**⌔∮ الاسم الوقتي شغال بالاصل**")
    JmdB.set_key("AUTONAME", "True")
    await event.eor("**⌔∮ تم بنجاح تشغيل الاسم الوقتي**", time=6)
    while JmdB.get_key("AUTONAME"):
        HM = time.strftime("%I:%M")
        name = f"{HM}"
        await event.client(UpdateProfileRequest(first_name=name))
        await asyncio.sleep(60)


@jmthon_cmd(pattern="بايو وقتي$")
async def autobio(event):
    if JmdB.get_key("AUTOBIO"):
        return await event.eor("**⌔∮ البايو الوقتي شغال بالاصل**")
    JmdB.set_key("AUTOBIO", "True")
    await event.eor("**⌔∮ تم بنجاح تشغيل البايو الوقتي**", time=6)
    BIOS = [
        "‏ويظنون أنَّك انتهِيتّ وأنت جمرٌ إذا اشتدت الرّيحُ أحرقت ظنَّهم",
        "isco is here"
        "محمد|isco "
    ]
    while JmdB.get_key("AUTOBIO"):
        BIOMSG = JmdB.get_key("MYBIO") or random.choice(BIOS)
        HM = time.strftime("%I:%M")
        name = f"{BIOMSG} | {HM}"
        await event.client(
            UpdateProfileRequest(
                about=name,
            )
        )
        await asyncio.sleep(60)



@jmthon_cmd(pattern=r"انهاء ([\s\S]*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if (
        input_str == "االوقت "
        or input_str == "الغي الوقت"
        or input_str == "الغي وقتي"
        or input_str == "وقت "
    ):
        if JmdB.get_key("AUTONAME"):
            JmdB.del_key("AUTONAME")
            await event.client(UpdateProfileRequest(first_name=NAME))
            return await event.eor("**- تم بنجاح ايقاف الوقت**")
        return await event.eor("**- الوقت مو شغال اصلا**")
    if input_str == "بايو وقتي" or input_str == " وقت البايو ":
        if JmdB.get_key("AUTOBIO"):
            JmdB.del_key("AUTOBIO")
            await event.client(UpdateProfileRequest(about=USERBIO))
            return await event.eor("**- تم بنجاح ايقاف الوقت بالبايو **")
        return await event.eor("**- الوقت بالبايو مو شغال اصلا**")
