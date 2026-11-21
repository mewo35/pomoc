import random  # Používá náhodné hodnoty pro déšť, chvění a úlomky.
import librosa  # Načítá zvuk a analyzuje jeho hlasitost a nárazy.
import numpy as np  # Provádí výpočty a vytváří obrazová data.
from pathlib import Path  # Sestavuje cestu k souboru nezávisle na aktuální složce.

from moviepy import AudioFileClip, VideoClip  # Vytváří video a připojuje k němu zvuk.
from PIL import Image, ImageDraw, ImageFilter  # Vytváří a kreslí jednotlivé snímky; ImageFilter se dále nepoužívá.

AUDIO_FILE = str(  # Uloží cestu ke zvukovému souboru jako text.
    Path.home()  # Začne v domovské složce aktuálního uživatele.
    / "Downloads"  # Přejde do složky Downloads.
    / "Breaking the Habit (Official Music Video) [HD UPGRADE] – Linkin Park.mp3"  # Vybere konkrétní MP3.
)
OUTPUT_FILE = "breaking_the_habit_full_video.mp4"  # Název vytvořeného videa.
WIDTH, HEIGHT = 720, 720  # Šířka a výška videa v pixelech.
FPS = 30  # Počet video snímků za sekundu.

print("1/3 Analyzing audio beats and energy...")  # Vypíše informaci o právě probíhající analýze.

if not Path(AUDIO_FILE).is_file() or Path(AUDIO_FILE).stat().st_size == 0:  # Ověří, že soubor existuje a není prázdný.
    raise FileNotFoundError(  # Zastaví program s vysvětlením, pokud zvuk chybí nebo je prázdný.
        f"Audio file is missing or empty: {AUDIO_FILE}. "  # Do chybové zprávy vloží cestu k souboru.
        "Put a valid MP3 or WAV file there."  # Poradí vložit platný zvukový soubor.
    )

y, sr = librosa.load(AUDIO_FILE, sr=22050)  # Načte zvuk jako vzorky y se vzorkovací frekvencí 22 050 Hz.
duration = librosa.get_duration(y=y, sr=sr)  # Spočítá délku zvuku v sekundách; tato proměnná se dále nepoužívá.

hop_length = int(sr / FPS)  # Určí počet zvukových vzorků odpovídající jednomu video snímku.
rms = librosa.feature.rms(y=y, hop_length=hop_length)[0]  # Vypočítá hlasitost zvuku v krátkých úsecích.
rms_norm = rms / (np.max(rms) + 1e-6)  # Normalizuje hlasitost přibližně do rozsahu 0 až 1.

onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length)  # Odhadne sílu zvukových nástupů, například úderů.
onset_norm = onset_env /  (np.max(onset_env) + 1e-6)  # Normalizuje sílu nástupů přibližně do rozsahu 0 až 1.

def spawn_shards(count=45):  # Vytvoří seznam náhodně rozmístěných pohybujících se úlomků.
    shards = []  # Připraví prázdný seznam úlomků.
    for _ in range(count):  # Opakuje tvorbu úlomku tolikrát, kolik určuje count.
        angle = random.uniform(0, 2 * np.pi)  # Vybere náhodný směr pohybu v radiánech.
        speed = random.uniform(5,22)  # Vybere počáteční rychlost úlomku.
        size = random.uniform(14, 48)  # Vybere velikost úlomku.
        pts = [  # Začne seznam bodů, které určují tvar úlomku.
            (random.uniform(-size, size), random.uniform(-size,size))  # Vytvoří jeden náhodný bod vůči středu úlomku.
            for _ in range(3)  # Vytvoří tři body, tedy přibližný trojúhelník.
        ]  # Ukončí seznam bodů úlomku.

        shards.append({  # Přidá nový úlomek se všemi jeho vlastnostmi do seznamu.
                "x": WIDTH / 2 + random.uniform(-90, 90),  # Nastaví počáteční vodorovnou polohu poblíž středu.
                "y": HEIGHT / 2 + random.uniform(-100, 80),  # Nastaví počáteční svislou polohu poblíž středu.
                "vx": np.cos(angle) * speed,  # Nastaví vodorovnou rychlost podle směru a rychlosti.
                "vy": np.sin(angle) * speed - random.uniform(1, 3),  # Nastaví svislou rychlost a mírně ji vychýlí vzhůru.
                "rot": random.uniform(0, 360),  # Nastaví počáteční natočení ve stupních.
                "vrot": random.uniform(-10, 10),  # Nastaví rychlost otáčení ve stupních na snímek.
                "scale": random.uniform(0.5, 1.2),  # Nastaví počáteční velikost úlomku.
                "pts": pts,  # Uloží trojúhelníkové body úlomku.
                "alpha": 230,  # Nastaví počáteční průhlednost (0 je průhledné, 255 neprůhledné).
        })  # Ukončí údaje pro tento úlomek.
        return shards  # Vrátí seznam už po prvním úlomku, protože return je uvnitř cyklu.

rain = [  # Vytvoří seznam částic představujících déšť.
        {"x": random.randint(0, WIDTH + 150), "y": random.randint(0, HEIGHT)}  # Rozmístí jednu kapku na náhodné místo.
        for _ in range(140)  # Vytvoří 140 kapek.
    ]  # Ukončí vytvoření seznamu deště.
active_shards = []  # Zatím neobsahuje žádné aktivní úlomky.
last_shatter_time = -10  # Uloží čas posledního rozbití; záporná hodnota dovolí první efekt hned.

bg = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)  # Vytvoří prázdný obraz pozadí s třemi barevnými kanály.
y_grad = np.linspace(0,1,HEIGHT)[:, None]  # Vytvoří svislý barevný přechod od 0 do 1.
bg[:, :, 0] = (12 + 26 * y_grad).astype(np.uint8)  # Nastaví červenou složku pozadí podle výšky.
bg[:, :, 1] = (30 + 50 * y_grad).astype(np.uint8)  # Nastaví zelenou složku pozadí podle výšky.
bg[:, :, 2] = (48 + 70 * y_grad).astype(np.uint8)  # Nastaví modrou složku pozadí podle výšky.
base_bg = Image.fromarray(bg).convert("RGBA")  # Převede pole barev na obrázek s alfa kanálem.

def make_frame(t):  # Vykreslí jeden video snímek pro čas t v sekundách.
    """generates each video frame dynamically synced to time t."""  # Popis funkce; tento text se nepoužívá při vykreslování.
    global active_shards, last_shatter_time  # Umožní funkci měnit sdílený seznam úlomků a čas posledního efektu.

    frame_idx = min(int(t * FPS), len(rms_norm) - 1)  # Převede čas na index hlasitosti a ohlídá konec seznamu.
    energy = float(rms_norm[frame_idx])  # Získá hlasitost zvuku pro aktuální snímek.
    onset_idx = min(int(t * FPS), len(onset_norm) - 1)  # Převede čas na index nástupu a ohlídá konec seznamu.
    beat = float(onset_norm[onset_idx])  # Získá sílu zvukového nástupu pro aktuální snímek.

    is_chorus = energy > 0.58  # Považuje hlasitý okamžik za refrénovou část.
    is_heavy_hit = beat > 0.65 and energy > 0.45  # Označí okamžik jako silný úder, pokud jsou nástup i hlasitost vysoké.

    just_shatterd = False  # Zapamatuje si, zda se právě spustil efekt rozbití.
    if is_heavy_hit and (t - last_shatter_time) > 3.5:  # Spustí efekt při silném úderu nejvýše jednou za 3,5 sekundy.
        active_shards = spawn_shards(50)  # Vytvoří 50 úlomků (funkce však kvůli odsazení vrátí jen jeden).
        last_shatter_time = t  # Uloží čas tohoto efektu.
        just_shatterd = True  # Označí aktuální snímek pro krátký záblesk.

    img = base_bg.copy()  # Zkopíruje pozadí, aby se další kresby nepřenášely do dalších snímků.
    draw = ImageDraw.Draw(img, "RGBA")  # Připraví kreslicí nástroj s podporou průhlednosti.
    cx, cy = WIDTH // 2, HEIGHT // 2+40  # Vypočítá střed postavy a posune ho o 40 pixelů dolů.

    shake_mag = int(18 * beat) if is_heavy_hit else int(4 * energy)  # Určí sílu chvění podle úderu nebo hlasitosti.
    shake_x = random.randint(-shake_mag, shake_mag)if shake_mag > 0 else 0  # Vybere náhodný vodorovný posun při chvění.
    shake_y = random.randint(-shake_mag, shake_mag)if shake_mag > 0 else 0  # Vybere náhodný svislý posun při chvění.

    halo_radius = int(200 + 130 * energy)  # Spočítá poloměr světelné záře podle hlasitosti.
    halo_alpha = int(45 + 75 * energy)  # Spočítá její průhlednost, ale tato hodnota se dále nepoužívá.
    draw.ellipse(  # Požádá Pillow o nakreslení oválu; bez fill nebo outline nebude ovál viditelný.
        [  # Následují souřadnice levého horního a pravého dolního rohu oválu.
            cx - halo_radius + shake_x,  # Levý okraj oválu.
            cy - halo_radius - 30 + shake_y,  # Horní okraj oválu.
            cx + halo_radius + shake_x,  # Pravý okraj oválu.
            cy + halo_radius - 30 + shake_y,  # Dolní okraj oválu.
        ],  # Ukončí souřadnice oválu.
    )  # Provede vykreslení oválu.

    if is_chorus:  # Přidá paprsky pouze při hlasité části.
        num_lines = int(45 * energy)  # Určí počet paprsků podle hlasitosti.
        for _ in range(num_lines):  # Vykreslí každý paprsek zvlášť.
            ang = random.uniform(0, 2 * np.pi)  # Vybere směr paprsku v radiánech.
            r1 = random.uniform(190, 290)  # Vybere náhodný vnitřní začátek paprsku.
            r2 = 540  # Nastaví vzdálený konec paprsku.
            draw.line(  # Vykreslí čáru mezi dvěma body.
                [  # Seznam souřadnic začátku a konce paprsku.
                    (cx + np.cos(ang) * r1, cy + np.sin(ang) * r1),  # Vypočítá vnitřní bod paprsku.
                    (cx + np.cos(ang) * r2, cy + np.sin(ang) * r2)  # Vypočítá vnější bod paprsku.
                ]  # Ukončí seznam bodů paprsku.
            )  # Provede vykreslení paprsku.

    ox, oy = cx + shake_x, cy + shake_y  # Nastaví střed postavy včetně aktuálního chvění.
    wind = np.sin(t * (5.0 + 6.0 * energy)) * (8 + 14 * energy)  # Vypočítá vlnivý pohyb podle času a hlasitosti.
    rim_color = (140, 230, 255, int(160 + 95 * energy))  # Nastaví světle modrou barvu obrysu včetně průhlednosti.

    jacket_pts = [  # Definuje body obrysu ramen a bundy postavy.
        (ox - 170, HEIGHT),  # Levý dolní bod bundy.
        (ox - 135, oy + 95),  # Levá spodní hrana bundy.
        (ox - 68, oy + 52),  # Bod u levého ramene.
        (ox - 90 + wind, oy + 10),  # Levá část límce posouvaná efektem větru.
        (ox - 38, oy + 38),  # Levá část horního okraje bundy.
        (ox + 38, oy + 38),  # Pravá část horního okraje bundy.
        (ox + 90 + wind, oy + 10),  # Pravá část límce posouvaná efektem větru.
        (ox + 68, oy + 52),  # Bod u pravého ramene.
        (ox + 135, oy + 95),  # Pravá spodní hrana bundy.
        (ox + 170, HEIGHT),  # Pravý dolní bod bundy.
    ]  # Ukončí seznam bodů bundy.

    draw.polygon(jacket_pts, fill = (10, 14, 20, 255))  # Vyplní bundu téměř černou barvou.
    draw.line(jacket_pts[1:-1], fill=rim_color, width=3)  # Vykreslí světelný obrys bundy bez spodních bodů.

    head_pts = [  # Definuje body obrysu hlavy.
        (ox - 48, oy - 68),  # Levý horní bod hlavy.
        (ox - 44, oy - 10),  # Levá spodní strana hlavy.
        (ox, oy + 22),  # Dolní střed hlavy.
        (ox + 44, oy - 10),  # Pravá spodní strana hlavy.
        (ox + 48, oy - 68),  # Pravý horní bod hlavy.
    ]  # Ukončí seznam bodů hlavy.

    draw.polygon(head_pts, fill=(14, 18, 26, 255))  # Vyplní hlavu tmavou barvou.
    draw.line(head_pts, fill=rim_color, width=2)  # Obtáhne hlavu světelnou čárou.

    spikes = [  # Definuje body tvořící stylizované špičaté vlasy.
        (ox - 52, oy - 52),  # Začátek obrysu vlasů vlevo.
        (ox - 88 + wind * 1.2, oy - 88),  # Levá vnější špička ovlivněná větrem.
        (ox - 56, oy - 80),  # Bod mezi levými špičkami.
        (ox - 74 + wind * 1.4, oy - 130),  # Další levá špička ovlivněná větrem.
        (ox - 32, oy - 102),  # Bod blíže ke středu vlevo.
        (ox - 20 + wind * 1.5, oy - 155),  # Vysoká špička vlevo od středu.
        (ox + 8, oy -110),  # Bod uprostřed vlasů.
        (ox + 32 + wind * 1.4, oy - 150),  # Vysoká špička vpravo od středu.
        (ox + 38, oy - 102),  # Bod blíže ke středu vpravo.
        (ox + 80 + wind * 1.3, oy - 120),  # Pravá horní špička ovlivněná větrem.
        (ox + 56, oy - 78),  # Bod mezi pravými špičkami.
        (ox + 92 + wind * 1.2, oy - 82),  # Pravá vnější špička ovlivněná větrem.
        (ox + 52, oy - 52),  # Konec obrysu vlasů vpravo.
    ]  # Ukončí seznam bodů vlasů.

    draw.polygon(spikes, fill=(8, 11, 16, 255))  # Vyplní vlasy téměř černou barvou.
    draw.line(spikes,fill=rim_color, width=2)  # Obtáhne vlasy světelnou čárou.

    glint_alpha = int(140 + 155 * energy)  # Spočítá průhlednost odlesku, ale tato hodnota se dále nepoužívá.
    draw.rectangle(  # Vykreslí malý světlý obdélník jako odlesk na hlavě.
        [ox + 6, oy - 48, ox + 31, oy - 31],  # Určí levý horní a pravý dolní roh obdélníku.
        fill=(215,248,255,255),  # Vyplní obdélník světle modrou neprůhlednou barvou.
        width=2,  # Nastaví šířku obrysu obdélníku.
    )  # Provede vykreslení odlesku.

    remaining_shards = []  # Připraví seznam úlomků, které po aktualizaci zůstanou viditelné.
    for s in active_shards:  # Projde všechny právě aktivní úlomky.
        s["x"] += s["vx"]  # Posune úlomek vodorovně podle jeho rychlosti.
        s["y"] += s["vy"]  # Posune úlomek svisle podle jeho rychlosti.
        s["vy"] += 0.35  # Přidá gravitaci, která úlomek postupně táhne dolů.
        s["rot"] += s["vrot"]  # Pootočí úlomek podle jeho rychlosti otáčení.
        s["scale"] += 0.015  # Každým snímkem úlomek mírně zvětší.
        s["alpha"] -= 3.5  # Každým snímkem úlomek postupně zprůhlední.

        if s["alpha"] > 0:  # Kreslí úlomek pouze do chvíle, než zcela zmizí.
            rad = np.radians(s["rot"])  # Převede jeho úhel ze stupňů na radiány.
            cos_r, sin_r = np.cos(rad), np.sin(rad)  # Předpočítá kosinus a sinus pro otočení bodů.
            poly = [  # Vytvoří seznam otočených a posunutých bodů úlomku.
                (  # Začne dvojici výsledných souřadnic bodu.
                    (px * cos_r - py * sin_r) * s["scale"] + s["x"],  # Otočí, zvětší a vodorovně posune bod.
                    (px * sin_r + py * cos_r) * s["scale"] + s["y"]  # Otočí, zvětší a svisle posune bod.
                )  # Ukončí dvojici výsledných souřadnic.
                for px, py in s["pts"]  # Provede výpočet pro každý původní bod úlomku.
            ]  # Ukončí seznam bodů mnohoúhelníku.
            a_int = int(s["alpha"])  # Převede průhlednost na celé číslo pro kreslicí funkci.

            draw.polygon(  # Vykreslí úlomek jako vyplněný mnohoúhelník s obrysem.
                poly,  # Předá souřadnice jeho vrcholů.
                fill=(190, 240, 255, int(a_int * 0.45)),  # Nastaví poloprůhlednou výplň.
                outline=(240, 252, 255, a_int),  # Nastaví světlejší obrys s aktuální průhledností.
            )  # Provede vykreslení úlomku.
            remaining_shards.append(s)  # Ponechá dosud viditelný úlomek pro další snímek.
    active_shards = remaining_shards  # Zahodí zmizelé úlomky a uloží seznam zbývajících.

    rain_speed = 16 + int(18 * energy)  # Zrychlí déšť podle hlasitosti hudby.
    for r in rain:  # Projde všechny kapky deště.
        r["x"] -= 4+ int(4 * energy)  # Posune kapku mírně doleva, rychleji při hlasitější hudbě.
        r["y"] += rain_speed  # Posune kapku směrem dolů.
        if r["y"] > HEIGHT:  # Zjistí, zda kapka spadla pod dolní okraj obrazu.
            r["y"] = random.randint(-80, 0)  # Vrátí kapku náhodně nad horní okraj.
            r["x"] = random.randint(0, WIDTH +150)  # Nastaví kapce novou náhodnou vodorovnou polohu.

        draw.line(  # Vykreslí kapku jako krátkou šikmou čáru.
            [(r["x"], r["y"]), (r["x"] - 6, r["y"] + 22)]  # Určí začátek a konec čáry kapky.
        )  # Provede vykreslení kapky.

    if just_shatterd:  # Přidá záblesk pouze ve snímku, kdy vznikly úlomky.
        flash = Image.new("RGBA", (WIDTH, HEIGHT), (230, 250, 255, 160))  # Vytvoří poloprůhlednou světlou vrstvu přes obraz.
        img = Image.alpha_composite(img,flash)  # Sloučí záblesk s aktuálním snímkem.

    return np.array(img.convert("RGB"))  # Převede hotový snímek na barevné pole, které očekává MoviePy.

print("2/3 Rendering full-song animation (this could take up to 5 minutes)")  # Oznámí začátek vykreslování videa.
audio_clip = AudioFileClip(AUDIO_FILE)  # Otevře zvukový soubor jako zvukovou stopu MoviePy.
video_clip = VideoClip(make_frame, duration=audio_clip.duration)  # Vytvoří video o délce zvukové stopy z funkce snímků.
final_clip = video_clip.with_audio(audio_clip)  # Připojí zvukovou stopu k videu.

print ("3/3 Exporting to mp4...")  # Oznámí, že se bude ukládat výsledné video.
final_clip.write_videofile(  # Vyrenderuje a uloží video do souboru.
    OUTPUT_FILE, fps=FPS, codec= "libx264", audio_codec ="aac"  # Nastaví název, snímkovou frekvenci a kodeky.
)  # Ukončí volání exportu videa.

print(f"done!!! Saved {OUTPUT_FILE}")  # Vypíše název výsledného souboru po dokončení exportu.
