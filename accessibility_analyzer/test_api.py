"""
공공데이터포털 API 테스트 스크립트
"""
import requests
import xml.etree.ElementTree as ET
from urllib.parse import urlencode, quote_plus, unquote
import json
import urllib3

# SSL 경고 비활성화
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# API 설정
API_KEY = unquote("")
BASE_URL = ""

def test_facility_list():
    """장애인편의시설 목록 조회 테스트"""
    # API 엔드포인트
    url = f"{BASE_URL}/getDisConvFaclList"
    
    # 요청 파라미터
    params = {
        'serviceKey': API_KEY,
        'pageNo': '1',
        'numOfRows': '10',
        'type': 'xml'
    }
    
    print("\n=== 장애인편의시설 목록 조회 테스트 ===")
    print(f"요청 URL: {url}")
    print(f"API 키: {API_KEY}")
    print(f"요청 파라미터: {params}")
    
    try:
        # API 요청 (HTTP 사용, SSL 검증 비활성화)
        session = requests.Session()
        session.verify = False
        response = session.get(url, params=params)
        print(f"\n응답 상태 코드: {response.status_code}")
        print(f"응답 헤더: {dict(response.headers)}")
        print(f"\n응답 내용:\n{response.text[:1000]}")  # 처음 1000자만 출력
        
        # XML 파싱
        root = ET.fromstring(response.content)
        
        # 오류 메시지 확인
        err_msg = root.find('.//errMsg')
        return_auth_msg = root.find('.//returnAuthMsg')
        return_reason_code = root.find('.//returnReasonCode')
        
        if err_msg is not None and err_msg.text == 'SERVICE ERROR':
            print(f"\nAPI 오류 발생:")
            print(f"오류 메시지: {err_msg.text}")
            print(f"인증 메시지: {return_auth_msg.text if return_auth_msg is not None else 'None'}")
            print(f"오류 코드: {return_reason_code.text if return_reason_code is not None else 'None'}")
            return
        
        # 시설 정보 출력
        items = root.findall('.//servList')
        print(f"\n검색된 시설 수: {len(items)}")
        
        for item in items[:3]:  # 처음 3개 시설만 출력
            print("\n시설 정보:")
            for child in item:
                print(f"{child.tag}: {child.text}")
                
    except Exception as e:
        print(f"\n오류 발생: {str(e)}")

def test_facility_detail():
    """장애인편의시설 상세 정보 조회 테스트"""
    # API 엔드포인트
    url = f"{BASE_URL}/getFacInfoOpenApiJpEvalInfoList"
    
    # 요청 파라미터 (예시 시설 ID 사용)
    params = {
        'serviceKey': API_KEY,
        'wfcltId': '4421010800-1-01490001',
        'type': 'xml'
    }
    
    print("\n=== 장애인편의시설 상세 정보 조회 테스트 ===")
    print(f"요청 URL: {url}")
    print(f"API 키: {API_KEY}")
    print(f"요청 파라미터: {params}")
    
    try:
        # API 요청 (HTTP 사용, SSL 검증 비활성화)
        session = requests.Session()
        session.verify = False
        response = session.get(url, params=params)
        print(f"\n응답 상태 코드: {response.status_code}")
        print(f"응답 헤더: {dict(response.headers)}")
        print(f"\n응답 내용:\n{response.text[:1000]}")  # 처음 1000자만 출력
        
        # XML 파싱
        root = ET.fromstring(response.content)
        
        # 오류 메시지 확인
        err_msg = root.find('.//errMsg')
        return_auth_msg = root.find('.//returnAuthMsg')
        return_reason_code = root.find('.//returnReasonCode')
        
        if err_msg is not None and err_msg.text == 'SERVICE ERROR':
            print(f"\nAPI 오류 발생:")
            print(f"오류 메시지: {err_msg.text}")
            print(f"인증 메시지: {return_auth_msg.text if return_auth_msg is not None else 'None'}")
            print(f"오류 코드: {return_reason_code.text if return_reason_code is not None else 'None'}")
            return
        
        # 시설 정보 출력
        items = root.findall('.//servList')
        print(f"\n검색된 시설 수: {len(items)}")
        
        for item in items:
            print("\n시설 정보:")
            for child in item:
                print(f"{child.tag}: {child.text}")
                
    except Exception as e:
        print(f"\n오류 발생: {str(e)}")

if __name__ == "__main__":
    print("공공데이터포털 API 테스트를 시작합니다...")
    test_facility_list()
    test_facility_detail() 