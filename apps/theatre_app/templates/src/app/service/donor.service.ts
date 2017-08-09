import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class DonorService {
  constructor(private _http: Http) {}

  createDonor(donor) {
    return this._http
      .post("/donor", donor)
      .map(data => data.json())
      .toPromise();
  }
  getDonor(donor) {
    return this._http.get("/donor", donor).map(data => data.json()).toPromise();
  }
  updateDonor(donor) {
    return this._http
      .patch(`/donor/${donor._id}`, donor)
      .map(data => data.json())
      .toPromise();
  }

  destroyDonor(id: string) {
    return this._http
      .delete(`/donor/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
