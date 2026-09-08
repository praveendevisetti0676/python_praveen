from exceptions import AuthenticationError


def login(username, password, logger):
    """Validate username and password."""

    logger.debug(
        f"Login attempt for user: {username}"
    )

    if not username or not password:
        logger.warning(
            "Username or password was empty"
        )

        raise AuthenticationError(
            "Username and password are required."
        )

    if username == "admin" and password == "admin123":

        logger.info(
            f"User logged in: {username}"
        )

        return True

    logger.error(
        f"Invalid login attempt for user: {username}"
    )

    raise AuthenticationError(
        "Invalid username or password."
    )


def logout(username, logger):
    """Log out the current user."""

    logger.info(
        f"User logged out: {username}"
    )

    print(
        f"{username} logged out successfully."
    )