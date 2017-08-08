import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class SpecialskillsService {
  constructor(private _http: Http) {}

  createSpecialskills(specialskills) {
    return this._http
      .post("/specialskills", specialskills)
      .map(data => data.json())
      .toPromise();
  }
  getSpecialskills(specialskills) {
    return this._http
      .get("/specialskill", specialskills)
      .map(data => data.json())
      .toPromise();
  }
  updateSpecialskills(specialskills) {
    return this._http
      .patch(`/specialskills/${specialskills._id}`, specialskills)
      .map(data => data.json())
      .toPromise();
  }

  destroySpecialskills(id: string) {
    return this._http
      .delete(`/specialskills/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
