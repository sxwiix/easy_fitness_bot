from typing import Dict
from telegram import Update


def print_update_data(update: Update):
    update_data = update.to_dict()
    for key, value in update_data.items():
        print(f"{key}: {value}")
# def extract_user_data_from_update(update: Update) -> Dict:
#     """ python-telegram-bot's Update instance --> User info """
#     user = update.effective_user.to_dict()
#     return dict(
#         user_id=user["id"],
#         is_blocked_bot=False,
#         **{
#             k: user[k]
#             for k in ["username", "first_name", "last_name", "language_code"]
#             if k in user and user[k] is not None
#         },
#     )