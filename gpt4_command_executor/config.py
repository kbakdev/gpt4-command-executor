from gpt4_command_executor import gpt3


def get_general_command(prompt):
    return gpt3.generate_terminal_command(prompt)


def get_git_command(prompt):
    git_prompt = f"git {prompt}"
    return gpt3.generate_terminal_command(git_prompt)


def get_gh_command(prompt):
    gh_prompt = f"github {prompt}"
    return gpt3.generate_terminal_command(gh_prompt)


def get_terminal_command(prompt):
    if prompt.startswith("??"):
        return get_general_command(prompt[2:].strip())
    elif prompt.startswith("git?"):
        return get_git_command(prompt[4:].strip())
    elif prompt.startswith("gh?"):
        return get_gh_command(prompt[3:].strip())
    else:
        return None
