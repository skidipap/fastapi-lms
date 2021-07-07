-- upgrade --
ALTER TABLE "user" RENAME COLUMN "is_active" TO "is_admin";
CREATE TABLE IF NOT EXISTS "userprofile" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "created_at" TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
    "full_name" VARCHAR(100),
    "phone" VARCHAR(100),
    "bio" VARCHAR(200),
    "user_id_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);;
-- downgrade --
ALTER TABLE "user" RENAME COLUMN "is_admin" TO "is_active";
DROP TABLE IF EXISTS "userprofile";
