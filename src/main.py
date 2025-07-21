import logging
import config
import phrases

from telegram import ChatMember, Update, User
from telegram.ext import (
    Application,
    ChatMemberHandler,
    ContextTypes,
)

logging.basicConfig(level=config.log_level())
logging.getLogger("httpx").setLevel(logging.WARNING)


def get_mention(user: User) -> str:
    if user.username != None:
        return '@' + user.username
    return user.first_name + (' ' + user.last_name if user.last_name != None else '')


async def handle_update(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    old_user = update.chat_member.old_chat_member
    new_user = update.chat_member.new_chat_member

    if new_user.status != ChatMember.LEFT:
        return

    logging.info(update.to_json())

    if getattr(old_user, 'is_anonymous', False) == True:
        return

    message = ''
    mention = get_mention(new_user.user)

    if hasattr(old_user, 'custom_title'):
        message = phrases.user_left_with_custom_title(mention, old_user.custom_title)
    else:
        message = phrases.user_left(mention)

    await update.effective_chat.send_message(message)


def main() -> None:
    application = Application.builder().token(config.token()).build()
    application.add_handler(ChatMemberHandler(handle_update, ChatMemberHandler.CHAT_MEMBER))
    application.run_polling(allowed_updates=Update.CHAT_MEMBER)


if __name__ == "__main__":
    main()
