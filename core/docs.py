import os
import json
import uuid
from typing import List, Dict

BASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'docs')


def ensure_dir():
    os.makedirs(BASE, exist_ok=True)
    index = os.path.join(BASE, 'index.json')
    if not os.path.exists(index):
        with open(index, 'w', encoding='utf-8') as f:
            json.dump([], f)


def _index_path():
    return os.path.join(BASE, 'index.json')


def list_docs() -> List[Dict]:
    ensure_dir()
    with open(_index_path(), 'r', encoding='utf-8') as f:
        return json.load(f)


def read_doc(doc_id: str) -> str:
    ensure_dir()
    path = os.path.join(BASE, f"{doc_id}.md")
    if not os.path.exists(path):
        return ''
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def create_doc(name: str, content: str = '') -> Dict:
    ensure_dir()
    slug = _slugify(name)
    slug = _ensure_unique_slug(slug)
    entry = {'id': slug, 'name': name}
    docs = list_docs()
    docs.insert(0, entry)
    with open(_index_path(), 'w', encoding='utf-8') as f:
        json.dump(docs, f)
    path = os.path.join(BASE, f"{slug}.md")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content or '')
    return entry


def update_doc(doc_id: str, name: str = None, content: str = None) -> Dict:
    ensure_dir()
    docs = list_docs()
    updated = None
    for idx, item in enumerate(docs):
        if item['id'] == doc_id:
            updated = item.copy()
            # handle rename
            if name is not None and name != item.get('name'):
                new_slug = _slugify(name)
                new_slug = _ensure_unique_slug(new_slug, exclude=doc_id)
                # rename file on disk
                old_path = os.path.join(BASE, f"{doc_id}.md")
                new_path = os.path.join(BASE, f"{new_slug}.md")
                try:
                    if os.path.exists(old_path):
                        os.rename(old_path, new_path)
                    else:
                        open(new_path, 'w', encoding='utf-8').close()
                except Exception:
                    pass
                # update index entry
                updated['id'] = new_slug
                updated['name'] = name
                docs[idx] = updated
            else:
                if name is not None:
                    item['name'] = name
                    updated['name'] = name
            break
    with open(_index_path(), 'w', encoding='utf-8') as f:
        json.dump(docs, f)
    # update content
    if updated is not None and content is not None:
        path = os.path.join(BASE, f"{updated['id']}.md")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    return updated


def delete_doc(doc_id: str) -> bool:
    ensure_dir()
    docs = list_docs()
    docs = [d for d in docs if d['id'] != doc_id]
    with open(_index_path(), 'w', encoding='utf-8') as f:
        json.dump(docs, f)
    path = os.path.join(BASE, f"{doc_id}.md")
    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception:
        pass
    return True


def _slugify(name: str) -> str:
    s = (name or '').strip()
    s = s.replace(' ', '_')
    # keep alnum, underscore, hyphen
    s = ''.join(c for c in s if c.isalnum() or c in ('_', '-'))
    s = s.lower()
    if not s:
        s = uuid.uuid4().hex
    return s


def _ensure_unique_slug(slug: str, exclude: str = None) -> str:
    ensure_dir()
    base = slug
    i = 1
    existing = {d['id'] for d in list_docs()}
    if exclude and exclude in existing:
        existing.remove(exclude)
    while slug in existing:
        slug = f"{base}-{i}"
        i += 1
    return slug
import os
import json
import uuid
from typing import List, Dict

BASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'docs')


def ensure_dir():
    os.makedirs(BASE, exist_ok=True)
    index = os.path.join(BASE, 'index.json')
    if not os.path.exists(index):
        with open(index, 'w', encoding='utf-8') as f:
            json.dump([], f)


def _index_path():
    return os.path.join(BASE, 'index.json')


def list_docs() -> List[Dict]:
    ensure_dir()
    with open(_index_path(), 'r', encoding='utf-8') as f:
        return json.load(f)


def read_doc(doc_id: str) -> str:
    ensure_dir()
    path = os.path.join(BASE, f"{doc_id}.md")
    if not os.path.exists(path):
        return ''
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def create_doc(name: str, content: str = '') -> Dict:
    ensure_dir()
    slug = _slugify(name)
    slug = _ensure_unique_slug(slug)
    entry = {'id': slug, 'name': name}
    docs = list_docs()
    docs.insert(0, entry)
    with open(_index_path(), 'w', encoding='utf-8') as f:
        json.dump(docs, f)
    path = os.path.join(BASE, f"{slug}.md")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content or '')
    return entry


def update_doc(doc_id: str, name: str = None, content: str = None) -> Dict:
    ensure_dir()
    docs = list_docs()
    updated = None
    for idx, item in enumerate(docs):
        if item['id'] == doc_id:
            updated = item.copy()
            # handle rename
            if name is not None and name != item.get('name'):
                new_slug = _slugify(name)
                new_slug = _ensure_unique_slug(new_slug, exclude=doc_id)
                # rename file on disk
                old_path = os.path.join(BASE, f"{doc_id}.md")
                new_path = os.path.join(BASE, f"{new_slug}.md")
                try:
                    if os.path.exists(old_path):
                        os.rename(old_path, new_path)
                    else:
                        open(new_path, 'w', encoding='utf-8').close()
                except Exception:
                    pass
                # update index entry
                updated['id'] = new_slug
                updated['name'] = name
                docs[idx] = updated
            else:
                if name is not None:
                    item['name'] = name
                    updated['name'] = name
            break
    with open(_index_path(), 'w', encoding='utf-8') as f:
        json.dump(docs, f)
    # update content
    if updated is not None and content is not None:
        path = os.path.join(BASE, f"{updated['id']}.md")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    return updated


def delete_doc(doc_id: str) -> bool:
    ensure_dir()
    docs = list_docs()
    docs = [d for d in docs if d['id'] != doc_id]
    with open(_index_path(), 'w', encoding='utf-8') as f:
        json.dump(docs, f)
    path = os.path.join(BASE, f"{doc_id}.md")
    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception:
        pass
    return True


def _slugify(name: str) -> str:
    s = (name or '').strip()
    s = s.replace(' ', '_')
    # keep alnum, underscore, hyphen
    s = ''.join(c for c in s if c.isalnum() or c in ('_', '-'))
    s = s.lower()
    if not s:
        s = uuid.uuid4().hex
    return s


def _ensure_unique_slug(slug: str, exclude: str = None) -> str:
    ensure_dir()
    base = slug
    i = 1
    existing = {d['id'] for d in list_docs()}
    if exclude and exclude in existing:
        existing.remove(exclude)
    while slug in existing:
        slug = f"{base}-{i}"
        i += 1
    return slug

