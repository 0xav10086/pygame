-- 角色表
CREATE TABLE Characters (
    CharacterID INT PRIMARY KEY,
    Name VARCHAR(100),
    Description TEXT,
    Attack INT,
    Life INT,
    RealisticDefense INT,
    MentalDefense INT,
    CriticalStrike INT,
    Attribute INT
);

INSERT INTO Characters (CharacterID, Name, Description, Attack, Life, RealisticDefense, MentalDefense, CriticalStrike, Attribute) VALUES
(780, '温妮弗雷德', '这里是角色描述', 1355, 8327, 718, 603, 254, 4);

-- 技能表
CREATE TABLE Skills (
    SkillID INT PRIMARY KEY,
    CharacterID INT,
    Name VARCHAR(100),
    StarLevel INT,
    Damage DECIMAL(5,2),
    BloodLoss DECIMAL(5,2),
    Type VARCHAR(50),
    Form VARCHAR(50),
    FOREIGN KEY (CharacterID) REFERENCES Characters(CharacterID)
);

-- 插入技能 '活力口袋'
INSERT INTO Skills (SkillID, CharacterID, Name, StarLevel, Damage, BloodLoss, Type, Form) VALUES
(7801, 780, '活力口袋', 1, 2.00, 0.10, 'debuff', 'unit_physics'),
(7802, 780, '活力口袋', 2, 3.00, 0.10, 'debuff', 'unit_physics'),
(7803, 780, '活力口袋', 3, 5.00, 0.10, 'debuff', 'unit_physics');

-- 插入技能 '古董扇贝'
INSERT INTO Skills (SkillID, CharacterID, Name, StarLevel, Damage, BloodLoss, Type, Form) VALUES
(7804, 780, '古董扇贝', 1, 1.60, 0.10, 'attack', 'group_physics'),
(7805, 780, '古董扇贝', 2, 2.50, 0.10, 'attack', 'group_physics'),
(7806, 780, '古董扇贝', 3, 4.00, 0.10, 'attack', 'group_physics');

-- 大招表
CREATE TABLE Ultimates (
    UltimateID INT PRIMARY KEY,
    CharacterID INT,
    Name VARCHAR(100),
    Damage DECIMAL(5,2),
    Vampire DECIMAL(5,2),
    Type VARCHAR(50),
    Form VARCHAR(50),
    FOREIGN KEY (CharacterID) REFERENCES Characters(CharacterID)
);

-- 插入大招 '埃克塞特的奇闻'
INSERT INTO Ultimates (UltimateID, CharacterID, Name, Damage, Vampire, Type, Form) VALUES
(7807, 780, '埃克塞特的奇闻', 3.00, 0.50, 'attack', 'group_physics');
