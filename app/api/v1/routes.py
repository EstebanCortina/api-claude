from flask import jsonify
from app.api.v1 import bp
from app.api.v1.resources.user_resource import register_user_resources

# Register resources
register_user_resources(bp)

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'})