def create_company_schema():
    query = """
    
    DROP TABLE IF EXISTS company;
    
    CREATE TABLE company
    (
        no_com			NUMERIC(5) SIREAL PRIMARY KEY,
        company_ko      VARCHAR(100),
        company_en      VARCHAR(100),
        company_ja      VARCHAR(100),
        tag_ko          VARCHAR(150),
        tag_en          VARCHAR(150),
        tag_ja          VARCHAR(150),
    ); --ON COMMIT DROP;
    
    
    --스프레드 시트로 insert문 작성
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(1, '원티드랩', 'Wantedlab', '', '태그_4|태그_20|태그_16','tag_4|tag_20|tag_16','タグ_4|タグ_20|タグ_16')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(2, '', 'OKAY.com', '', '태그_24|태그_27|태그_4','tag_24|tag_27|tag_4','タグ_24|タグ_27|タグ_4')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(3, '이상한마케팅', '', '', '태그_25|태그_6|태그_14|태그_9','tag_25|tag_6|tag_14|tag_9','タグ_25|タグ_6|タグ_14|タグ_9')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(4, '인포뱅크', 'infobank', '', '태그_25','tag_25','タグ_25')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(5, '아이씨그룹', '', '', '태그_1|태그_23|태그_28|태그_14','tag_1|tag_23|tag_28|tag_14','タグ_1|タグ_23|タグ_28|タグ_14')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(6, '딤딤섬 대구점', '', '', '태그_22|태그_29|태그_2|태그_13','tag_22|tag_29|tag_2|tag_13','タグ_22|タグ_29|タグ_2|タグ_13')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(7, '파운데이션엑스', '', '', '태그_8','tag_8','タグ_8')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(8, '엣지랭크', '', '', '태그_5|태그_11|태그_26|태그_1','tag_5|tag_11|tag_26|tag_1','タグ_5|タグ_11|タグ_26|タグ_1')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(9, '커넥티어', '', '', '태그_11|태그_21','tag_11|tag_21','タグ_11|タグ_21')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(10, '자버(Jober)', '', '', '태그_2|태그_16','tag_2|tag_16','タグ_2|タグ_16')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(11, '앨리스헬스케어', '', '', '태그_13|태그_5|태그_12','tag_13|tag_5|tag_12','タグ_13|タグ_5|タグ_12')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(12, '(주)몬스터스튜디오', '', '', '태그_19','tag_19','タグ_19')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(13, 'SM Entertainment Japan', '', '株式会社SM Entertainment Japan', '태그_23|태그_11|태그_15','tag_23|tag_11|tag_15','タグ_23|タグ_11|タグ_15')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(14, '쿠차', '', '', '태그_27|태그_5|태그_26','tag_27|tag_5|tag_26','タグ_27|タグ_5|タグ_26')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(15, 'ZMP', '', '株式会社ZMP', '태그_10|태그_2|태그_21|태그_24','tag_10|tag_2|tag_21|tag_24','タグ_10|タグ_2|タグ_21|タグ_24')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(16, '몽키랩', '', '', '태그_7|태그_23|태그_28','tag_7|tag_23|tag_28','タグ_7|タグ_23|タグ_28')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(17, '와이케이비앤씨', '', '', '태그_14|태그_29|태그_6','tag_14|tag_29|tag_6','タグ_14|タグ_29|タグ_6')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(18, '코츠테크놀로지', '', '', '태그_12|태그_2','tag_12|tag_2','タグ_12|タグ_2')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(19, '비고라이브', '', '', '태그_13|태그_19','tag_13|tag_19','タグ_13|タグ_19')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(20, '크로싱', '', '', '태그_21|태그_30|태그_12|태그_28','tag_21|tag_30|tag_12|tag_28','タグ_21|タグ_30|タグ_12|タグ_28')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(21, '트리노드', '', '', '태그_7|태그_19|태그_12|태그_17','tag_7|tag_19|tag_12|tag_17','タグ_7|タグ_19|タグ_12|タグ_17')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(22, '와이즈키즈(wisekids)', '', '', '태그_1|태그_9|태그_17|태그_14','tag_1|tag_9|tag_17|tag_14','タグ_1|タグ_9|タグ_17|タグ_14')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(23, 'Obelab', '', '', '태그_6','tag_6','タグ_6')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(24, '', 'Foodpanda', '', '태그_26','tag_26','タグ_26')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(25, '웹티즌', '', '', '태그_28|태그_25|태그_7|태그_13','tag_28|tag_25|tag_7|tag_13','タグ_28|タグ_25|タグ_7|タグ_13')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(26, '마이셀럽스', '', '', '태그_2|태그_8|태그_22|태그_27','tag_2|tag_8|tag_22|tag_27','タグ_2|タグ_8|タグ_22|タグ_27')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(27, '데이터얼라이언스(DataAlliance)', '', '', '태그_27|태그_6|태그_11','tag_27|tag_6|tag_11','タグ_27|タグ_6|タグ_11')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(28, '쿼드자산운용', '쿼드자산운용', '', '태그_24|태그_23|태그_26|태그_29','tag_24|tag_23|tag_26|tag_29','タグ_24|タグ_23|タグ_26|タグ_29')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(29, '주식회사 링크드코리아', '', '', '태그_12|태그_6|태그_8','tag_12|tag_6|tag_8','タグ_12|タグ_6|タグ_8')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(30, '주렁주렁(zoolungzoolung)', '', '', '태그_30|태그_17|태그_18','tag_30|tag_17|tag_18','タグ_30|タグ_17|タグ_18')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(31, '', 'Amore Pacific_TEST', '', '태그_17|태그_27|태그_28|태그_6','tag_17|tag_27|tag_28|tag_6','タグ_17|タグ_27|タグ_28|タグ_6')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(32, '', 'Luna Marketing Group', '', '태그_2|태그_18','tag_2|tag_18','タグ_2|タグ_18')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(33, '동신항운', '', '', '태그_26','tag_26','タグ_26')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(34, '히숲', '', '', '태그_11|태그_17|태그_7|태그_14','tag_11|tag_17|tag_7|tag_14','タグ_11|タグ_17|タグ_7|タグ_14')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(35, 'COVENANT', 'COVENANT', '', '태그_10|태그_3','tag_10|tag_3','タグ_10|タグ_3')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(36, '젠틀파이', '', '', '태그_18|태그_17|태그_4|태그_14','tag_18|tag_17|tag_4|tag_14','タグ_18|タグ_17|タグ_4|タグ_14')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(37, '아크로고스', '', '', '태그_15|태그_29|태그_27','tag_15|tag_29|tag_27','タグ_15|タグ_29|タグ_27')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(38, '페르소나미디어', 'Persona Media', '', '태그_26|태그_13','tag_26|tag_13','タグ_26|タグ_13')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(39, '', 'Rejoice Pregnancy', '', '태그_22|태그_30|태그_7|태그_4','tag_22|tag_30|tag_7|tag_4','タグ_22|タグ_30|タグ_7|タグ_4')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(40, '', 'The Wave', '', '태그_3','tag_3','タグ_3')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(41, '', 'CoCoon Foundation', '', '태그_26','tag_26','タグ_26')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(42, '스트라다월드와이드(Strada)', '', '', '태그_9|태그_14|태그_11|태그_13','tag_9|tag_14|tag_11|tag_13','タグ_9|タグ_14|タグ_11|タグ_13')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(43, '도빗(Dobbit)', '', '', '태그_29|태그_18|태그_21','tag_29|tag_18|tag_21','タグ_29|タグ_18|タグ_21')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(44, '지란지교시큐리티', '', '', '태그_26|태그_24|태그_10|태그_27','tag_26|tag_24|tag_10|tag_27','タグ_26|タグ_24|タグ_10|タグ_27')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(45, '캠퍼스멘토', '', '', '태그_29','tag_29','タグ_29')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(46, '삼일제약', '', '', '태그_2|태그_22','tag_2|tag_22','タグ_2|タグ_22')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(47, '제이에이치개발', '', '', '태그_27|태그_25|태그_6|태그_14','tag_27|tag_25|tag_6|tag_14','タグ_27|タグ_25|タグ_6|タグ_14')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(48, '오케이코인코리아', '', '', '태그_3|태그_25','tag_3|tag_25','タグ_3|タグ_25')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(49, '그릿연구소', '', '', '태그_25','tag_25','タグ_25')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(50, '세계정부 世界政府', '', '', '태그_15|태그_19|태그_11','tag_15|tag_19|tag_11','タグ_15|タグ_19|タグ_11')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(51, '투게더앱스', '', '', '태그_22|태그_10|태그_4|태그_28','tag_22|tag_10|tag_4|tag_28','タグ_22|タグ_10|タグ_4|タグ_28')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(52, 'Dream Agility', 'Dream Agility', '', '태그_19','tag_19','タグ_19')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(53, '대성시스템', '', '', '태그_2|태그_19','tag_2|tag_19','タグ_2|タグ_19')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(54, '바이럴네이션', '', '', '태그_8|태그_6|태그_20|태그_26','tag_8|tag_6|tag_20|tag_26','タグ_8|タグ_6|タグ_20|タグ_26')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(55, '오가나셀', '', '', '태그_11|태그_1','tag_11|tag_1','タグ_11|タグ_1')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(56, '디토나인', '', '', '태그_25|태그_29|태그_14','tag_25|tag_29|tag_14','タグ_25|タグ_29|タグ_14')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(57, '', 'Haulio', '', '태그_3','tag_3','タグ_3')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(58, '대상홀딩스(주) - existing', '', '', '태그_23','tag_23','タグ_23')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(59, '만나씨이에이', '', '', '태그_15','tag_15','タグ_15')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(60, '지오코리아(페루관광청)', 'GEOCM Co.', 'GEOCM', '태그_28|태그_17','tag_28|tag_17','タグ_28|タグ_17')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(61, 'KFC Korea', '', '', '태그_17|태그_19','tag_17|tag_19','タグ_17|タグ_19')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(62, '까브드뱅(Cave de Vin)', '', '', '태그_2|태그_10|태그_21','tag_2|tag_10|tag_21','タグ_2|タグ_10|タグ_21')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(63, '홈스토리생활', '', '', '태그_7|태그_20','tag_7|tag_20','タグ_7|タグ_20')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(64, '아이엠에이치씨(IMHC)', '', '', '태그_4|태그_30|태그_19|태그_28','tag_4|tag_30|tag_19|tag_28','タグ_4|タグ_30|タグ_19|タグ_28')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(65, '플라이트그래프-탈퇴', '', '', '태그_30|태그_17|태그_9','tag_30|tag_17|tag_9','タグ_30|タグ_17|タグ_9')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(66, 'YG PLUS', '', '', '태그_1|태그_16|태그_5','tag_1|tag_16|tag_5','タグ_1|タグ_16|タグ_5')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(67, '우리말소프트', '', '', '태그_13|태그_27|태그_24','tag_13|tag_27|tag_24','タグ_13|タグ_27|タグ_24')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(68, '아로마티카', '', '', '태그_29','tag_29','タグ_29')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(69, '', 'Private Organization', '', '태그_24','tag_24','タグ_24')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(70, '스피링크', '', '', '태그_19|태그_9','tag_19|tag_9','タグ_19|タグ_9')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(71, 'Onion Ground', '', '', '태그_6|태그_2','tag_6|tag_2','タグ_6|タグ_2')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(72, '브레이브팝스', '', '', '태그_28','tag_28','タグ_28')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(73, 'Bidalgo', '', '', '태그_3|태그_13','tag_3|tag_13','タグ_3|タグ_13')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(74, '티엠씨케이', '', '', '태그_1|태그_26|태그_19|태그_17','tag_1|tag_26|tag_19|tag_17','タグ_1|タグ_26|タグ_19|タグ_17')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(75, '(주) 휴톰-중복', '', '', '태그_14|태그_15','tag_14|tag_15','タグ_14|タグ_15')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(76, '', 'Chengbao', '', '태그_24|태그_16|태그_19|태그_29','tag_24|tag_16|tag_19|tag_29','タグ_24|タグ_16|タグ_19|タグ_29')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(77, '헬프미', '', '', '태그_26|태그_11|태그_16','tag_26|tag_11|tag_16','タグ_26|タグ_11|タグ_16')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(78, '(주) 새론다이내믹스', '', '', '태그_15|태그_14|태그_30|태그_29','tag_15|tag_14|tag_30|tag_29','タグ_15|タグ_14|タグ_30|タグ_29')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(79, '마상소프트', '', '', '태그_12','tag_12','タグ_12')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(80, '(주)아임블록', '', '', '태그_25','tag_25','タグ_25')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(81, '(주)이모션글로벌-중복', '', '', '태그_13|태그_21|태그_28','tag_13|tag_21|tag_28','タグ_13|タグ_21|タグ_28')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(82, 'Altagram', '', '', '태그_25|태그_26','tag_25|tag_26','タグ_25|タグ_26')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(83, '이베스트투자증권', '', '', '태그_1|태그_20','tag_1|tag_20','タグ_1|タグ_20')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(84, '소굿마케팅', '', '', '태그_9|태그_10|태그_5','tag_9|tag_10|tag_5','タグ_9|タグ_10|タグ_5')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(85, '', 'Grab', '', '태그_1','tag_1','タグ_1')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(86, '', 'HK Yau', '', '태그_30','tag_30','タグ_30')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(87, '더락포트컴퍼니코리아-중복', '', '', '태그_7','tag_7','タグ_7')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(88, '휴마트컴퍼니', '', '', '태그_16|태그_29','tag_16|tag_29','タグ_16|タグ_29')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(89, '디센터', '', '', '태그_29|태그_7','tag_29|tag_7','タグ_29|タグ_7')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(90, '컬쳐히어로', '', '', '태그_11','tag_11','タグ_11')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(91, '보비어스코리아', '', '', '태그_11|태그_8|태그_3|태그_4','tag_11|tag_8|tag_3|tag_4','タグ_11|タグ_8|タグ_3|タグ_4')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(92, '베이글랩스', '', '', '태그_8|태그_18|태그_16','tag_8|tag_18|tag_16','タグ_8|タグ_18|タグ_16')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(93, '', 'Katalis Digital', '', '태그_2|태그_16|태그_6|태그_18','tag_2|tag_16|tag_6|tag_18','タグ_2|タグ_16|タグ_6|タグ_18')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(94, '애디터(Additor)', '', '', '태그_11|태그_2','tag_11|tag_2','タグ_11|タグ_2')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(95, '', 'Avanade Asia Pte Ltd', '', '태그_8|태그_29|태그_15|태그_11','tag_8|tag_29|tag_15|tag_11','タグ_8|タグ_29|タグ_15|タグ_11')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(96, '500V2', '', '', '태그_11|태그_27','tag_11|tag_27','タグ_11|タグ_27')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(97, '플라이앤컴퍼니(푸드플라이)', '', '', '태그_29','tag_29','タグ_29')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(98, '영우디지탈-중복', '', '', '태그_14|태그_15|태그_7|태그_11','tag_14|tag_15|tag_7|tag_11','タグ_14|タグ_15|タグ_7|タグ_11')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(99, '', 'Machipopo Inc.', '', '태그_19|태그_10|태그_4|태그_20','tag_19|tag_10|tag_4|tag_20','タグ_19|タグ_10|タグ_4|タグ_20')";
    insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(100, '시니어벤처스', '', '', '태그_20|태그_21|태그_6','tag_20|tag_21|tag_6','タグ_20|タグ_21|タグ_6')";
    """
    return query

def select_nm_company_auto():
    # select test
    query = '''
    select * 
    from company
    where company_ko LIKE %(nm_com)s
    '''
    return query

def select_nm_company_info():
    # select test

    query = '''
    select * 
    from company
    where company_ko = %(nm_com)s
       or company_en = %(nm_com)s
       or company_ja = %(nm_com)s
    --select case when %(nation)s = 'KR' then company_ko
    --            when %(nation)s = 'EN' then company_en
    --            when %(nation)s = 'JA' then company_ja
    --            else company_ko
    --            end as nm_com
    --from company
    '''
    return query

def insert_new_company():
    # select test

    query = '''
        insert into company(no_com, company_ko, company_en, company_ja, tag_ko, tag_en, tag_ja) values(101, '가영컴퍼니', 'youngcorparation', '', '태그_2','tag_22','タグ_2222')"; 
    '''
    return query