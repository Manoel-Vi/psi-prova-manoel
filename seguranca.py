from flask import flash, redirect, session, url_for


def exigir_login():
    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))
    return None
