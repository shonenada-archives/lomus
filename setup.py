from setuptools import setup, find_packages


install_requires = [l.strip() for l in open("requirements.txt", "r")]


metadata = {"name": "szu.fm",
            "version": "0.1",
            "packages": find_packages(),
            "author": "shonenada",
            "author_email": "shonenada@gmail.com",
            "url": "http://fm.shonenada.com",
            "zip_safe": False,
            "platforms": ["linux"],
            "package_data": {"": ["*.html", "*.jpg", "*.png", "*.css", "*.js",
                                  "*.ico", "*.coffee", "*.less"]},
            "install_requires": install_requires,
            "description": "FM in SZU."}


if __name__ == "__main__":
    setup(**metadata)
