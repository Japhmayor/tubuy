# Contributing to tubuy

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to `tubuy`.
These are just guidelines, not rules, use your best judgment and feel free to propose changes to this document in a pull request.

#### Table Of Contents

[What should I know before I get started?](#what-should-i-know-before-i-get-started)
  * [Code of Conduct](#code-of-conduct)
  * [Design Decisions](#project-decisions)

[How Can I Contribute?](#how-can-i-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Suggesting Enhancements](#suggesting-enhancements)
  * [Your First Code Contribution](#your-first-code-contribution)
  * [Pull Requests](#pull-requests)

[Styleguides](#styleguides)
  * [Git Commit Messages](#git-commit-messages)

[Additional Notes](#additional-notes)
  * [Issue and Pull Request Labels](#issue-and-pull-request-labels)

## What should I know before I get started?

### Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code.
Please report unacceptable behavior to [mutembei.collin@gmail.com](mailto:mutembei.collin@gmail.com).

### Project Decisions

When we make a significant decision in how we maintain the project and what we can or cannot support, we will be documenting them in [decisions](DECISIONS.md). If you have a question around how we do things, check to see if it is documented there. If it is *not* documented there, kindly start a conversation around your conversation in the projects [slack](http://solublecode-slack.herokuapp.com/) channel.

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report for `tubuy`. Following these guidelines helps maintainers and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

Before creating bug reports, please check [this list](#before-submitting-a-bug-report) as you might find out that you don't need to create one. When you are creating a bug report, please [include as many details as possible](#how-do-i-submit-a-good-bug-report). If you'd like, you can use [this template](#template-for-submitting-bug-reports) to structure the information.

#### Before Submitting A Bug Report

* **Perform a [search](https://github.com/SolubleCode/tubuy/issues)** to see if the problem has already been reported. If it has, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Bug Report?

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue on the projects [repository](https://github.com/SolubleCode/tubuy) and provide the following information.

Explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible. For example, start by explaining how you started `tubuy`, e.g. which command exactly you used in the terminal. When listing steps, **don't just say what you did, but explain how you did it**. For example, if you passed input that caused an unexpected error, explain which keys you pressed, and if not so how did you go about it?
* **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem. You can use [this tool](http://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
* **If the Chrome's developer tools pane is shown without you triggering it**, that normally means that an exception was thrown. The Console tab will include an entry for the exception. Expand the exception so that the stack trace is visible, and provide the full exception and stack trace in a [code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines) and as a screenshot.
* **If the problem wasn't triggered by a specific action**, describe what you were doing before the problem happened and share more information using the guidelines below.

Provide more context by answering these questions:

* **Can you reproduce the problem?**
* **Did the problem start happening recently** (e.g. after pulling recent code) or was this always a problem?
* If the problem started happening recently, **can you reproduce the problem in an older commit of the code?** What's the most recent commit in which the problem doesn't happen?
* **Can you reliably reproduce the issue?** If not, provide details about how often the problem happens and under which conditions it normally happens.

Include details about your configuration and environment:

* **Which version of Python are you using?** You can get the exact version by running `python --version` or `python3 --version` in your terminal.
* **What's the name and version of the OS you're using**?
* **Are you running `tubuy` in a virtual environment?** If so, which virtual environment package are you using?
* **Which packages do you have installed?** You can get that list by running `pip freeze` or `pip3 freeze`.

#### Template For Submitting Bug Reports

    [Short description of problem here]

    **Reproduction Steps:**

    1. [First Step]
    2. [Second Step]
    3. [Other Steps...]

    **Expected behavior:**

    [Describe expected behavior here]

    **Observed behavior:**

    [Describe observed behavior here]

    **Screenshots and GIFs**

    ![Screenshots and GIFs which follow reproduction steps to demonstrate the problem](url)

    **Python version:** [Enter Python version here]
    **OS and version:** [Enter OS name and version here]

    **Installed packages:**

    [List of installed packages here]

    **Additional information:**

    * Problem can be reliably reproduced, doesn't happen randomly: [Yes/No]
    * Problem started happening recently, didn't happen in an older version of tubuy: [Yes/No]

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for `tubuy`, including completely new features and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion :pencil: and find related suggestions :mag_right:.

Before creating enhancement suggestions, please check [this list](#before-submitting-an-enhancement-suggestion) as you might find out that you don't need to create one. When you are creating an enhancement suggestion, please [include as many details as possible](#how-do-i-submit-a-good-enhancement-suggestion). If you'd like, you can use [this template](#template-for-submitting-enhancement-suggestions) to structure the information.

#### Before Submitting An Enhancement Suggestion

* **Check if there's already a Python [package](https://pypi.python.org/pypi?%3Aaction=browse) which provides that enhancement.** Perform an informed assessment as to why we should or not add it to the projects dependencies.
* **Perform a [search](https://github.com/SolubleCode/tubuy/issues)** to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue on the projects [repository](https://github.com/SolubleCode/tubuy) and provide the following information:

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps**. Include copy/pasteable snippets which you use in those examples, as [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Include screenshots and animated GIFs** which help you demonstrate the steps or point out the part of `tubuy` which the suggestion is related to. You can use [this tool](http://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
* **Explain why this enhancement would be useful** to most `tubuy` users and isn't something that can or should be implemented as a python package of its own.
* **List some other products or projects where this enhancement exists.**
* **Which version of Python are you using?** You can get the exact version by running `python --version` or `python3 --version` in your terminal.
* **Specify the name and version of the OS you're using.**

#### Template For Submitting Enhancement Suggestions

    [Short description of suggestion]

    **Steps which explain the enhancement**

    1. [First Step]
    2. [Second Step]
    3. [Other Steps...]

    **Current and suggested behavior**

    [Describe current and suggested behavior here]

    **Why would the enhancement be useful to most users**

    [Explain why the enhancement would be useful to most users]

    [List some other text editors or applications where this enhancement exists]

    **Screenshots and GIFs**

    ![Screenshots and GIFs which demonstrate the steps or part of tubuy the enhancement suggestion is related to](url)

    **Python Version:** [Enter python version here]
    **OS and Version:** [Enter OS name and version here]

### Your First Code Contribution
Unsure where to begin contributing to `tubuy`? You can start by looking through these `beginner` and `help-wanted` issues:

* [Beginner issues][beginner] - issues which should only require a few lines of code, and a test or two.
* [Help wanted issues][help-wanted] - issues which should be a bit more involved than `beginner` issues.

Both issue lists are sorted by total number of comments. While not perfect, number of comments is a reasonable proxy for impact a given change will have.

If you want to read about contributing to open source, we recommend this [GitHub guide](https://guides.github.com/activities/contributing-to-open-source/) as a start.

**Working on your first Pull Request?**  
You can learn how from this *free* course [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)

### Pull Requests

* Include screenshots and animated GIFs in your pull request whenever possible.
* Follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide.
* Include thoughtfully-worded, well-structured
  tests in the `./tests` folder. Run them using `python manage.py test`.
* Document new code using docstrings.
* End files with a newline.
* Place imports in the following order:
    * standard library imports
    * related third party imports
    * local application/library specific imports

## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally
* Consider starting the commit message with an applicable emoji:
    * :art: `:art:` when improving the format/structure of the code
    * :racehorse: `:racehorse:` when improving performance
    * :non-potable_water: `:non-potable_water:` when plugging memory leaks
    * :memo: `:memo:` when writing docs
    * :penguin: `:penguin:` when fixing something on Linux
    * :apple: `:apple:` when fixing something on macOS
    * :checkered_flag: `:checkered_flag:` when fixing something on Windows
    * :bug: `:bug:` when fixing a bug
    * :fire: `:fire:` when removing code or files
    * :green_heart: `:green_heart:` when fixing the CI build
    * :white_check_mark: `:white_check_mark:` when adding tests
    * :lock: `:lock:` when dealing with security
    * :arrow_up: `:arrow_up:` when upgrading dependencies
    * :arrow_down: `:arrow_down:` when downgrading dependencies
    * :shirt: `:shirt:` when removing linter warnings


## Additional Notes

### Issue and Pull Request Labels

This section lists the labels we use to help us track and manage issues and pull requests.

[GitHub search](https://help.github.com/articles/searching-issues/) makes it easy to use labels for finding groups of issues or pull requests you're interested in. For example, you might be interested in [open issues across `SolubleCode/tubuy` which are labeled as bugs, but still need to be reliably reproduced](https://github.com/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+user%3ASolubleCode+label%3Abug+label%3Aneeds-reproduction) or perhaps [open pull requests in `SolubleCode/tubuy` which haven't been reviewed yet](https://github.com/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Apr+repo%3ASolubleCode%2Ftubuy+comments%3A0). To help you find issues and pull requests, each label is listed with search links for finding open items with that label in `SolubleCode/tubuy`. We  encourage you to read about [other search filters](https://help.github.com/articles/searching-issues/) which will help you write more focused queries.

The labels are loosely grouped by their purpose, but it's not required that every issue have a label from every group or that an issue can't have more than one label from the same group.

Please open an issue on `SolubleCode/tubuy` if you have suggestions for new labels.

#### Type of Issue and Issue State

| Label name | `SolubleCode/tubuy` :mag_right: | Description |
| --- | --- | --- |
| `enhancement` | [search][search-tubuy-repo-label-enhancement] | Feature requests. |
| `bug` | [search][search-tubuy-repo-label-bug] | Confirmed bugs or reports that are very likely to be bugs. |
| `question` | [search][search-tubuy-repo-label-question] | Questions more than bug reports or feature requests (e.g. how do I do X). |
| `feedback` | [search][search-tubuy-repo-label-feedback] | General feedback more than bug reports or feature requests. |
| `help-wanted` | [search][search-tubuy-repo-label-help-wanted] | The `tubuy` core team would appreciate help from the community in resolving these issues. |
| `beginner` | [search][search-tubuy-repo-label-beginner] | Less complex issues which would be good first issues to work on for users who want to contribute to `tubuy`. |
| `more-information-needed` | [search][search-tubuy-repo-label-more-information-needed] | More information needs to be collected about these problems or feature requests (e.g. steps to reproduce). |
| `needs-reproduction` | [search][search-tubuy-repo-label-needs-reproduction] | Likely bugs, but haven't been reliably reproduced. |
| `blocked` | [search][search-tubuy-repo-label-blocked] | Issues blocked on other issues. |
| `duplicate` | [search][search-tubuy-repo-label-duplicate] | Issues which are duplicates of other issues, i.e. they have been reported before. |
| `wontfix` | [search][search-tubuy-repo-label-wontfix] | The `tubuy` core team has decided not to fix these issues for now, either because they're working as intended or for some other reason. |
| `invalid` | [search][search-tubuy-repo-label-invalid] | Issues which aren't valid (e.g. user errors). |
| `package-idea` | [search][search-tubuy-repo-label-package-idea] | Feature request which might be good candidates for new packages. |
| `wrong-repo` | [search][search-tubuy-repo-label-wrong-repo] | Issues reported on the wrong repository. |

#### Topic Categories

| Label name | `SolubleCode/tubuy` :mag_right: | Description |
| --- | --- | --- |
| `windows` | [search][search-tubuy-repo-label-windows] | Related to `tubuy` running on Windows. |
| `linux` | [search][search-tubuy-repo-label-linux] | Related to `tubuy` running on Linux. |
| `mac` | [search][search-tubuy-repo-label-mac] | Related to `tubuy` running on macOS. |
| `documentation` | [search][search-tubuy-repo-label-documentation] | Related to any type of documentation. |
| `performance` | [search][search-tubuy-repo-label-performance] | Related to performance. |
| `security` | [search][search-tubuy-repo-label-security] | Related to security. |
| `ui` | [search][search-tubuy-repo-label-ui] | Related to visual design. |
| `api` | [search][search-tubuy-repo-label-api] | Related to `tubuy`'s public APIs. |
| `uncaught-exception` | [search][search-tubuy-repo-label-uncaught-exception] | Issues about uncaught exceptions |
| `crash` | [search][search-tubuy-repo-label-crash] | Reports of `tubuy` completely crashing. |
| `auto-indent` | [search][search-tubuy-repo-label-auto-indent] | Related to auto-indenting text. |
| `encoding` | [search][search-tubuy-repo-label-encoding] | Related to character encoding. |
| `network` | [search][search-tubuy-repo-label-network] | Related to network problems or working with remote files (e.g. on network drives). |
| `git` | [search][search-tubuy-repo-label-git] | Related to Git functionality (e.g. problems with gitignore files or with showing the correct file status). |

#### `SolubleCode/tubuy` Topic Categories

| Label name | `SolubleCode/tubuy` :mag_right: | Description |
| --- | --- | --- | --- |
| `deprecation-help` | [search][search-tubuy-repo-label-deprecation-help] | Issues for helping package authors remove usage of deprecated packages. |
| `electron` | [search][search-tubuy-repo-label-electron] | Issues that require changes to [Electron](https://electron.atom.io) to fix or implement. |

#### Pull Request Labels

| Label name | `SolubleCode/tubuy` :mag_right: | Description
| --- | --- | --- | --- |
| `work-in-progress` | [search][search-tubuy-repo-label-work-in-progress] | Pull requests which are still being worked on, more changes will follow. |
| `needs-review` | [search][search-tubuy-repo-label-needs-review] | Pull requests which need code review, and approval from maintainers or `tubuy` core team. |
| `under-review` | [search][search-tubuy-repo-label-under-review] | Pull requests being reviewed by maintainers or `tubuy` core team. |
| `requires-changes` | [search][search-tubuy-repo-label-requires-changes] | Pull requests which need to be updated based on review comments and then reviewed again. |
| `needs-testing` | [search][search-tubuy-repo-label-needs-testing] | Pull requests which need manual testing. |

[search-tubuy-repo-label-enhancement]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Aenhancement
[search-tubuy-repo-label-bug]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Abug
[search-tubuy-repo-label-question]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Aquestion
[search-tubuy-repo-label-feedback]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Afeedback
[search-tubuy-repo-label-help-wanted]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Ahelp-wanted
[search-tubuy-repo-label-beginner]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Abeginner
[search-tubuy-repo-label-more-information-needed]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Amore-information-needed
[search-tubuy-repo-label-needs-reproduction]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Aneeds-reproduction
[search-tubuy-repo-label-windows]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Awindows
[search-tubuy-repo-label-linux]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Alinux
[search-tubuy-repo-label-mac]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Amac
[search-tubuy-repo-label-documentation]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Adocumentation
[search-tubuy-repo-label-performance]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Aperformance
[search-tubuy-repo-label-security]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Asecurity
[search-tubuy-repo-label-ui]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Aui
[search-tubuy-repo-label-api]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Aapi
[search-tubuy-repo-label-crash]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Acrash
[search-tubuy-repo-label-auto-indent]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Aauto-indent
[search-tubuy-repo-label-encoding]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Aencoding
[search-tubuy-repo-label-network]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Anetwork
[search-tubuy-repo-label-uncaught-exception]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Auncaught-exception
[search-tubuy-repo-label-git]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Agit
[search-tubuy-repo-label-blocked]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Ablocked
[search-tubuy-repo-label-duplicate]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Aduplicate
[search-tubuy-repo-label-wontfix]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Awontfix
[search-tubuy-repo-label-invalid]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Ainvalid
[search-tubuy-repo-label-package-idea]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Apackage-idea
[search-tubuy-repo-label-wrong-repo]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Awrong-repo
[search-tubuy-repo-label-deprecation-help]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Adeprecation-help
[search-tubuy-repo-label-electron]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Aelectron
[search-tubuy-repo-label-work-in-progress]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Awork-in-progress
[search-tubuy-repo-label-needs-review]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Aneeds-review
[search-tubuy-repo-label-under-review]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Aunder-review
[search-tubuy-repo-label-requires-changes]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Arequires-changes
[search-tubuy-repo-label-needs-testing]: https://github.com/issues?q=is%3Aopen+is%3Aissue+repo%3ASolubleCode%2Ftubuy+label%3Aneeds-testing

[beginner]:https://github.com/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3Abeginner+label%3Ahelp-wanted+repo%3ASolubleCode%2Ftubuy+sort%3Acomments-desc
[help-wanted]:https://github.com/issues?q=is%3Aopen+is%3Aissue+label%3Ahelp-wanted+repo%3ASolubleCode%2Ftubuy+sort%3Acomments-desc
