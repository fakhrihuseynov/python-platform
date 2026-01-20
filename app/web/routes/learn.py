from flask import Blueprint, render_template, request, jsonify
from core.lessons import get_lessons
from core.docs import list_docs, read_doc, create_doc, update_doc, delete_doc, load_folders, save_folders

bp = Blueprint("learn", __name__)


@bp.route("/")
def list_lessons():
    lessons = get_lessons()
    return render_template("learn.html", lessons=lessons)


@bp.route('/docs')
def docs_index():
    return render_template('docs.html')


@bp.route('/docs/files', methods=['GET'])
def docs_files():
    return jsonify(list_docs())


@bp.route('/docs/folders', methods=['GET', 'POST'])
def docs_folders():
    if request.method == 'GET':
        mapping, names = load_folders()
        return jsonify({'mapping': mapping, 'names': names})
    else:
        data = request.get_json() or {}
        mapping = data.get('mapping', {})
        names = data.get('names', [])
        ok = save_folders(mapping, names)
        return jsonify({'ok': bool(ok)})


@bp.route('/docs/file', methods=['POST'])
def docs_create():
    data = request.get_json() or {}
    name = data.get('name', 'Untitled')
    content = data.get('content', '')
    entry = create_doc(name, content)
    return jsonify(entry)


@bp.route('/docs/file/<doc_id>', methods=['GET', 'PUT', 'DELETE'])
def docs_file(doc_id):
    if request.method == 'GET':
        content = read_doc(doc_id)
        return jsonify({'id': doc_id, 'content': content})
    if request.method == 'PUT':
        data = request.get_json() or {}
        name = data.get('name')
        content = data.get('content')
        entry = update_doc(doc_id, name=name, content=content)
        return jsonify(entry)
    if request.method == 'DELETE':
        delete_doc(doc_id)
        return jsonify({'ok': True})
