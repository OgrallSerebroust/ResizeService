<h3 align="center">
    Resize service
</h3>
<div align="center">
    Web app to resize images recived via a link
</div>

---

<div align="center">
    <img src="https://img.shields.io/badge/license-PolyForm Noncommercial-orange?labelColor=555555&color=007EC6" alt="License">
    <img alt="Dynamic TOML Badge" src="https://img.shields.io/badge/dynamic/toml?url=https://raw.githubusercontent.com/OgrallSerebroust/ResizeService/refs/heads/main/pyproject.toml&query=$.[project][version]&label=version&labelColor=555555&color=007EC6">
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/OgrallSerebroust/ResizeService?labelColor=555555&color=007EC6">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/OgrallSerebroust/ResizeService?labelColor=555555&color=007EC6">
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/OgrallSerebroust/ResizeService?labelColor=555555&color=007EC6">
    <img alt="GitHub Issues" src="https://img.shields.io/github/issues/OgrallSerebroust/ResizeService?labelColor=555555&color=007EC6">
    <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/OgrallSerebroust/ResizeService?labelColor=555555&color=007EC6">
</div>
<details>
    <summary>
        <strong>
            Table of Contents 📜
        </strong>
    </summary>

- [Features :muscle:](#features-muscle)
- [Getting started :seedling:](#getting-started-seedling)
  - [Prerequisites :page\_with\_curl:](#prerequisites-page_with_curl)
  - [Installation :inbox\_tray:](#installation-inbox_tray)
- [Built with :wrench:](#built-with-wrench)

</details>

## Features :muscle:

* **Link availability:** You don't need to download images before use service. You can just paste link on desired image.
* **Most used extensions:** "Resize service" supports a list of most used image extensions, such as: ".png", ".jpg", ".jpeg", ".gif", ".raw", ".tiff", ".tif", ".JPG", ".PNG" and ".JPEG".
* **Not just increasing:** Our "Resize service" otherwise from other free services supports not only increasing the image size, but also reducing the image size without losing quality.
* **Batch of images per try:** Our "Resize service" supports bulk processing. You can paste a list of images links to input, and service proccess each image. After you will see result of work with all links, also if any link is not valid, it will be noticed.
* **Accessibility via link:** After processing "Resize service" shows a list of links to result images. Service saves images about one month and you can access images via its links to download it, or paste where are you want.


## Getting started :seedling:

If you want to start up "Resize service" by own. You can relax. That project is default django project. And you can start up it like other django projects.

### Prerequisites :page_with_curl:

Before you begin, ensure you have the following installed on your machine:

- **Python** (version 3.13.7 or higher)
- **uv** (Python Package Manager)

### Installation :inbox_tray:

To install the project, follow these steps:

1. Clone this repository to your local machine:
   ```bash
    git clone https://github.com/OgrallSerebroust/ResizeService.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ResizeService
    ```
3. Install the dependencies:
    ```bash
    uv sync
    ```
4. Setup the database:
    ```bash
    python ResizeService/manage.py migrate
    ```
5. Collect staticfiles of project:
   ```bash
    python ResizeService/manage.py collectstatic
    ```
6. Run server:
   ```bash
    python ResizeService/manage.py runserver
    ```


## Built with :wrench:

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](#)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)](#)
[![JavaScript](	https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](#)
[![JQuery](	https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)](#)
[![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](#)
[![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](#)
[![Bootstrap](	https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](#)
[![MySql](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)](#)
[![SQLite](https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](#)
