import os
import urllib.request
import zipfile
import tarfile
import sys

DEPS_DIR = "deps"

DEPENDENCIES = [
    {"name": "SDL2", "url": "https://www.libsdl.org/release/SDL2-devel-2.26.5-VC.zip", "extract": True},
    {"name": "GLEW", "url": "https://github.com/nigels-com/glew/releases/download/glew-2.2.0/glew-2.2.0-win32.zip", "extract": True},
    {"name": "FreeType", "url": "https://download.savannah.gnu.org/releases/freetype/freetype-2.13.1.tar.gz", "extract": True},
    {"name": "libpng", "url": "https://download.sourceforge.net/libpng/libpng-1.6.40.tar.gz", "extract": True},
    {"name": "SDL2_mixer", "url": "https://www.libsdl.org/projects/SDL_mixer/release/SDL2_mixer-devel-2.6.3-VC.zip", "extract": True},
    {"name": "libvorbis", "url": "https://downloads.xiph.org/releases/vorbis/libvorbis-1.3.7.tar.gz", "extract": True},
    {"name": "Box2D", "url": "https://github.com/erincatto/box2d/archive/refs/heads/master.zip", "extract": True},
    {"name": "zlib", "url": "https://zlib.net/zlib-1.2.13.tar.gz", "extract": True},
    {"name": "rapidjson", "url": "https://github.com/Tencent/rapidjson/archive/refs/heads/master.zip", "extract": True},
]

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def download_file(url, dest):
    print(f"⬇ Downloading {os.path.basename(dest)} ...")
    try:
        urllib.request.urlretrieve(url, dest)
        print(f"✔ Downloaded {os.path.basename(dest)}")
    except Exception as e:
        print(f"❌ Failed to download {url}: {e}")
        sys.exit(1)

def extract_file(path, extract_to):
    print(f"🗜 Extracting {os.path.basename(path)} ...")
    try:
        if path.endswith(".zip"):
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
        elif path.endswith(".tar.gz") or path.endswith(".tgz"):
            with tarfile.open(path, 'r:gz') as tar_ref:
                tar_ref.extractall(extract_to)
        print(f"✔ Extracted {os.path.basename(path)}")
    except Exception as e:
        print(f"❌ Failed to extract {path}: {e}")
        sys.exit(1)

def download_all_deps():
    ensure_dir(DEPS_DIR)
    for dep in DEPENDENCIES:
        filename = os.path.join(DEPS_DIR, dep["url"].split("/")[-1])
        if not os.path.exists(filename):
            download_file(dep["url"], filename)
        else:
            print(f"✔ {dep['name']} already downloaded")

        if dep.get("extract", False):
            extract_dir = os.path.join(DEPS_DIR, dep["name"])
            if not os.path.exists(extract_dir):
                ensure_dir(extract_dir)
                extract_file(filename, extract_dir)
            else:
                print(f"✔ {dep['name']} already extracted")

    print("\n✅ All dependencies are downloaded and ready!")

if __name__ == "__main__":
    download_all_deps()
