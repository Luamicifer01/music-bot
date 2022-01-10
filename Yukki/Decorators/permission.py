from typing import Dict, List, Union

from Yukki import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
            return await message.reply_text(
                "mereko permission mangta hai :\n"
                + "\n- **can_manage_voice_chats:**voice chats chalane ke liye"
                + "\n- **can_delete_messages:** tum log ka search hatane ke liye"
                + "\n- **can_invite_users**: apne advik ko bulane ke liye *blush*"
            )
        if not a.can_manage_voice_chats:
            await message.reply_text(
                "mereko permission hi nahi diya *sad*."
                + "\n**Permission:** __MANAGE VOICE CHATS__"
            )
            return
        if not a.can_delete_messages:
            await message.reply_text(
                "mereko permission hi nahi diya *sad*."
                + "\n**Permission:** __DELETE MESSAGES__"
            )
            return
        if not a.can_invite_users:
            await message.reply_text(
                "mereko permission hi nahi diya *sad*."
                + "\n**Permission:** __INVITE USERS VIA LINK__"
            )
            return
        return await mystic(_, message)

    return wrapper
